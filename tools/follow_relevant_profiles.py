#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"
API_VERSION = "2026-03-10"


def request(method, url, token, payload=None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "ger1e-profile-follower",
            **({"Content-Type": "application/json"} if payload is not None else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            return resp.status, (json.loads(body) if body else None)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {url} failed: HTTP {exc.code}: {body}") from exc


def graphql(token, query, variables):
    _, body = request("POST", GRAPHQL, token, {"query": query, "variables": variables})
    if body.get("errors"):
        raise RuntimeError("GitHub GraphQL error: " + json.dumps(body["errors"], ensure_ascii=False))
    return body["data"]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def targets(repo_catalog, provider_catalog, self_login):
    owners = set()
    for item in repo_catalog.get("repositories", []):
        if item.get("status") != "ACTIVE":
            continue
        if item.get("provenance") in {"LEGACY", "TRAINING-LAB"}:
            continue
        repo = item.get("repo", "")
        if "/" in repo:
            owners.add(repo.split("/", 1)[0])

    for provider in provider_catalog.get("providers", []):
        for field in ("official_repositories", "community_integrations"):
            for repo in provider.get(field, []):
                if "/" in repo:
                    owners.add(repo.split("/", 1)[0])

    return sorted(x for x in owners if x.lower() != self_login.lower())


def account_type(login, token):
    _, body = request("GET", f"{API}/users/{login}", token)
    return body.get("type"), body.get("node_id")


def follow_user(login, token):
    request("PUT", f"{API}/user/following/{login}", token)


def follow_org(login, node_id, token):
    if not node_id:
        data = graphql(
            token,
            "query($login:String!){organization(login:$login){id}}",
            {"login": login},
        )
        node_id = (data.get("organization") or {}).get("id")
    if not node_id:
        raise RuntimeError(f"Could not resolve organization node id for {login}")
    graphql(
        token,
        "mutation($id:ID!){followOrganization(input:{organizationId:$id}){organization{login}}}",
        {"id": node_id},
    )


def main():
    parser = argparse.ArgumentParser(description="Follow relevant GitHub profiles from canonical catalogs")
    parser.add_argument("--repos", default="catalog/repos.yaml")
    parser.add_argument("--providers", default="catalog/providers.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    token = os.environ.get("FOLLOW_TOKEN", "")
    if not token and not args.dry_run:
        print("FOLLOW_TOKEN is required. Use a fine-grained PAT with Followers: write, or a classic PAT with user:follow.", file=sys.stderr)
        return 2

    self_login = "ger1e"
    repo_catalog = load_json(args.repos)
    provider_catalog = load_json(args.providers)
    selected = targets(repo_catalog, provider_catalog, self_login)
    print(f"Relevant profiles selected: {len(selected)}")

    failures = []
    for login in selected:
        if args.dry_run:
            print(f"DRY {login}")
            continue
        try:
            kind, node_id = account_type(login, token)
            if kind == "Organization":
                follow_org(login, node_id, token)
                print(f"ORG  {login}: followed")
            elif kind == "User":
                follow_user(login, token)
                print(f"USER {login}: followed")
            else:
                print(f"SKIP {login}: unsupported account type {kind}")
        except Exception as exc:
            failures.append((login, str(exc)))
            print(f"FAIL {login}: {exc}", file=sys.stderr)

    if failures:
        print(f"Completed with {len(failures)} failure(s).", file=sys.stderr)
        return 1
    print("Relevant profile follow pass: complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
