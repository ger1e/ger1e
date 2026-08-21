#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Iterable

GITHUB_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
LINK_RE = re.compile(r"\[([^\]]+)\]\((https://github\.com/[^)]+)\)(?:\s+[—-]\s+(.+))?")
VALID_PROVENANCE = {"OFFICIAL", "CANONICAL", "COMMUNITY", "LEGACY", "TRAINING-LAB"}
VALID_RISK = {"SAFE-REFERENCE", "ACTIVE-SECURITY-TOOL", "OFFENSIVE-DUAL-USE", "LIVE-MALWARE", "VULNERABLE-LAB"}
VALID_STATUS = {"ACTIVE", "ARCHIVED", "MISSING", "PRIVATE", "RENAMED", "UNKNOWN"}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "uncategorized"


def normalize_repo_url(url: str):
    match = GITHUB_RE.search(url)
    if not match:
        return None
    owner, repo = match.groups()
    repo = repo.removesuffix('.git')
    full = f"{owner}/{repo}"
    return full, f"https://github.com/{full}"


def infer_provenance(source: str, description: str) -> str:
    text = f"{source} {description}".lower()
    if "community" in text or "third-party" in text:
        return "COMMUNITY"
    if "archived" in text or "legacy" in text:
        return "LEGACY"
    if source == "api-tools" and ("official" in text or "canonical" in text):
        return "OFFICIAL"
    return "CANONICAL"


def classify_risk(repo: str, description: str) -> str:
    text = f"{repo} {description}".lower()
    live = ("live malware", "malware samples", "thezoo")
    labs = ("deliberately vulnerable", "vulnerable app", "training lab", "security lab", "goat")
    offensive = (
        "penetration-testing", "pentesting", "exploit", "c2 framework", "credential", "red-team",
        "adversary", "payload", "phishing-simulation", "authentication testing", "mimikatz", "rubeus",
        "nishang", "empire", "sliver", "havoc", "mythic", "sqlmap", "hydra", "metasploit"
    )
    active_tool = ("scanner", "framework", "platform", "client", "sdk", "cli", "analysis", "forensics", "monitoring")
    if any(x in text for x in live):
        return "LIVE-MALWARE"
    if any(x in text for x in labs):
        return "VULNERABLE-LAB"
    if any(x in text for x in offensive):
        return "OFFENSIVE-DUAL-USE"
    if any(x in text for x in active_tool):
        return "ACTIVE-SECURITY-TOOL"
    return "SAFE-REFERENCE"


def extract_repositories(markdown: str, source: str):
    category = "uncategorized"
    rows = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            category = slugify(line[3:].strip())
            continue
        match = LINK_RE.search(line)
        if not match:
            continue
        _, url, description = match.groups()
        norm = normalize_repo_url(url)
        if not norm:
            continue
        repo, root = norm
        desc = (description or "").strip().rstrip(".")
        rows.append({
            "repo": repo,
            "url": root,
            "category": category,
            "description": desc,
            "sources": [source],
            "provenance": infer_provenance(source, desc),
            "risk": classify_risk(repo, desc),
            "status": "ACTIVE",
        })
    return rows


def merge_entries(entries: Iterable[dict]):
    merged = {}
    for item in entries:
        key = item["repo"].lower()
        if key not in merged:
            merged[key] = dict(item)
            merged[key]["sources"] = list(item.get("sources", []))
            continue
        cur = merged[key]
        cur["sources"] = sorted(set(cur.get("sources", [])) | set(item.get("sources", [])))
        if not cur.get("description") and item.get("description"):
            cur["description"] = item["description"]
        if cur.get("category") == "uncategorized" and item.get("category"):
            cur["category"] = item["category"]
        if item.get("provenance") == "OFFICIAL":
            cur["provenance"] = "OFFICIAL"
        if item.get("risk") in {"LIVE-MALWARE", "OFFENSIVE-DUAL-USE", "VULNERABLE-LAB"}:
            cur["risk"] = item["risk"]
    return sorted(merged.values(), key=lambda x: (x["category"], x["repo"].lower()))


def validate_catalog(catalog: dict):
    errors = []
    seen = set()
    for i, item in enumerate(catalog.get("repositories", []), start=1):
        repo = item.get("repo", "")
        key = repo.lower()
        if key in seen:
            errors.append(f"duplicate repo: {repo}")
        seen.add(key)
        if item.get("provenance") not in VALID_PROVENANCE:
            errors.append(f"invalid provenance at entry {i}: {item.get('provenance')}")
        if item.get("risk") not in VALID_RISK:
            errors.append(f"invalid risk at entry {i}: {item.get('risk')}")
        if item.get("status") not in VALID_STATUS:
            errors.append(f"invalid status at entry {i}: {item.get('status')}")
        norm = normalize_repo_url(item.get("url", ""))
        if not norm or norm[0].lower() != key:
            errors.append(f"repo/url mismatch: {repo}")
    return errors


def load_catalog(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_catalog(path: Path, catalog: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bootstrap(root: Path, manifest: dict):
    rows = []
    for src in manifest.get("bootstrap_sources", []):
        p = root / src["file"]
        rows.extend(extract_repositories(p.read_text(encoding="utf-8"), source=src["id"]))
    items = merge_entries(rows)
    overrides = manifest.get("overrides", {})
    for item in items:
        item.update(overrides.get(item["repo"], {}))
    return {
        "schema": manifest.get("schema", "ger1e-security-catalog/v1"),
        "generated_from": [s["id"] for s in manifest.get("bootstrap_sources", [])],
        "last_verified": manifest.get("last_verified"),
        "repositories": items,
    }


def render_catalog(catalog: dict) -> str:
    groups = defaultdict(list)
    for item in catalog.get("repositories", []):
        groups[item["category"]].append(item)
    lines = [
        "# Security repository catalog", "", "Generated from `catalog/repos.yaml`. Do not hand-edit this file.", "",
        f"**Repositories:** {len(catalog.get('repositories', []))}",
        f"**Last verified:** {catalog.get('last_verified') or 'not yet verified'}", "",
        "Legend: `OFFICIAL/CANONICAL/COMMUNITY/LEGACY/TRAINING-LAB` · `SAFE-REFERENCE/ACTIVE-SECURITY-TOOL/OFFENSIVE-DUAL-USE/LIVE-MALWARE/VULNERABLE-LAB`.", ""
    ]
    for category in sorted(groups):
        lines += [f"## {category.replace('-', ' ').title()}", ""]
        for item in sorted(groups[category], key=lambda x: x["repo"].lower()):
            meta = f"`{item['provenance']}` · `{item['risk']}` · `{item['status']}`"
            desc = f" — {item['description']}" if item.get("description") else ""
            aliases = f" · aliases: {', '.join(item['aliases'])}" if item.get("aliases") else ""
            lines.append(f"- [{item['repo']}]({item['url']}) — {meta}{aliases}{desc}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def github_repo_state(repo: str, token: str | None):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "ger1e-security-catalog", **({"Authorization": f"Bearer {token}"} if token else {})},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {"status": "MISSING"}
        raise
    status = "ARCHIVED" if data.get("archived") else "ACTIVE"
    if data.get("private"):
        status = "PRIVATE"
    return {"status": status, "full_name": data.get("full_name") or repo, "default_branch": data.get("default_branch"), "archived": bool(data.get("archived")), "html_url": data.get("html_url")}


def apply_repo_state(item: dict, state: dict):
    updated = dict(item)
    old_name = updated.get("repo", "")
    canonical = state.get("full_name") or old_name
    if canonical and canonical.lower() != old_name.lower():
        aliases = set(updated.get("aliases", []))
        if old_name:
            aliases.add(old_name)
        updated["aliases"] = sorted(aliases, key=str.lower)
        updated["repo"] = canonical
        updated["url"] = state.get("html_url") or f"https://github.com/{canonical}"
    updated["status"] = state.get("status", "UNKNOWN")
    return updated


def render_health(catalog: dict, checked: list[dict]) -> str:
    counts = defaultdict(int)
    for row in checked:
        counts[row["status"]] += 1
    date = catalog.get("last_verified") or dt.date.today().isoformat()
    lines = ["# Repository health", "", f"**Atlas verification:** {date}", f"**Repositories checked:** {len(checked)}", f"**Healthy:** {counts['ACTIVE']}", f"**Archived:** {counts['ARCHIVED']}", f"**Missing:** {counts['MISSING']}", f"**Private:** {counts['PRIVATE']}", "", "Generated by `tools/catalog.py`. Exact star counts are intentionally excluded.", ""]
    exceptions = [r for r in checked if r["status"] != "ACTIVE"]
    if exceptions:
        lines += ["## Exceptions", ""]
        for row in exceptions:
            lines.append(f"- `{row['repo']}` — `{row['status']}`")
        lines.append("")
    return "\n".join(lines)


def cmd_validate(args):
    catalog = load_catalog(Path(args.catalog))
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"catalog valid: {len(catalog.get('repositories', []))} repositories")
    return 0


def cmd_build(args):
    catalog = load_catalog(Path(args.catalog))
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    Path(args.output).write_text(render_catalog(catalog), encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


def cmd_bootstrap(args):
    root = Path(args.root)
    manifest_path = Path(args.catalog)
    catalog = bootstrap(root, load_catalog(manifest_path))
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.write:
        write_catalog(manifest_path, catalog)
        print(f"bootstrapped {len(catalog['repositories'])} repositories")
    else:
        print(json.dumps(catalog, indent=2, ensure_ascii=False))
    return 0


def cmd_health(args):
    path = Path(args.catalog)
    catalog = load_catalog(path)
    catalog["last_verified"] = dt.date.today().isoformat()
    checked = []
    refreshed = []
    for item in catalog.get("repositories", []):
        state = github_repo_state(item["repo"], args.token)
        updated = apply_repo_state(item, state)
        refreshed.append(updated)
        checked.append({"repo": updated["repo"], "status": updated["status"]})
    catalog["repositories"] = sorted(refreshed, key=lambda x: (x["category"], x["repo"].lower()))
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.write:
        write_catalog(path, catalog)
        Path(args.report).write_text(render_health(catalog, checked), encoding="utf-8")
    print(render_health(catalog, checked))
    return 0


def main():
    parser = argparse.ArgumentParser(description="Maintain the ger1e security repository catalog")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("validate"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.set_defaults(func=cmd_validate)
    p = sub.add_parser("build"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--output", default="CATALOG.md"); p.set_defaults(func=cmd_build)
    p = sub.add_parser("bootstrap"); p.add_argument("--root", default="."); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--write", action="store_true"); p.set_defaults(func=cmd_bootstrap)
    p = sub.add_parser("health"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--report", default="LAST-VERIFIED.md"); p.add_argument("--token"); p.add_argument("--write", action="store_true"); p.set_defaults(func=cmd_health)
    args = parser.parse_args(); raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
