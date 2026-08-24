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
SOURCE_FILES = (
    {"id": "atlas", "file": "SECURITY-REPOS.md"},
    {"id": "soc-manual", "file": "SOC-MANUAL-REPOS.md"},
    {"id": "api-tools", "file": "API-TOOLS-REPOS.md"},
)
VALID_PROVIDER_AUTH = {"NONE", "API_KEY_HEADER", "API_KEY_QUERY", "BEARER", "TOKEN_HEADER", "MIXED", "UNKNOWN"}
VALID_PROVIDER_ACCESS = {"OPEN", "FREE", "FREEMIUM", "PAID", "MIXED", "UNKNOWN"}
VALID_PROVIDER_PROVENANCE = {"OFFICIAL", "VENDOR-DOCS", "COMMUNITY-VERIFIED"}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "uncategorized"


def normalize_repo_url(url: str):
    match = GITHUB_RE.search(url)
    if not match:
        return None
    owner, repo = match.groups()
    repo = repo.removesuffix(".git")
    full = f"{owner}/{repo}"
    return full, f"https://github.com/{full}"


def infer_provenance(source: str, description: str) -> str:
    text = f"{source} {description}".lower()
    if "training-lab" in text or "training lab" in text:
        return "TRAINING-LAB"
    if "community" in text or "third-party" in text:
        return "COMMUNITY"
    if "archived" in text or "legacy" in text:
        return "LEGACY"
    if source.startswith("api-tools") and ("official" in text or "canonical" in text):
        return "OFFICIAL"
    return "CANONICAL"


def classify_risk(repo: str, description: str) -> str:
    text = f"{repo} {description}".lower()
    live = ("live malware", "malware samples", "thezoo")
    labs = ("deliberately vulnerable", "vulnerable app", "training lab", "security lab", "goat")
    offensive = (
        "penetration-testing", "pentesting", "exploit", "c2 framework", "credential", "red-team",
        "adversary", "payload", "phishing-simulation", "authentication testing", "mimikatz", "rubeus",
        "nishang", "empire", "sliver", "havoc", "mythic", "sqlmap", "hydra", "metasploit",
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
        if line.startswith("#### "):
            category = slugify(line[5:].strip())
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
        context_source = f"{source}:{category}"
        rows.append({
            "repo": repo,
            "url": root,
            "category": category,
            "description": desc,
            "sources": [source],
            "provenance": infer_provenance(context_source, desc),
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
        elif cur.get("provenance") not in {"OFFICIAL", "COMMUNITY"} and item.get("provenance") == "COMMUNITY":
            cur["provenance"] = "COMMUNITY"
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


def source_rows(root: Path):
    rows = []
    for src in SOURCE_FILES:
        p = root / src["file"]
        if not p.exists():
            raise FileNotFoundError(f"missing catalog source: {p}")
        rows.extend(extract_repositories(p.read_text(encoding="utf-8"), source=src["id"]))
    return rows


def reconcile_catalog(root: Path, current: dict):
    parsed = merge_entries(source_rows(root))
    existing = {}
    for old in current.get("repositories", []):
        existing[old.get("repo", "").lower()] = old
        for alias in old.get("aliases", []):
            existing.setdefault(alias.lower(), old)

    reconciled = []
    for item in parsed:
        old = existing.get(item["repo"].lower())
        if not old:
            reconciled.append(item)
            continue

        merged = dict(old)
        canonical_changed = old.get("repo", "").lower() != item["repo"].lower()
        for key in ("category", "description", "sources", "provenance", "risk"):
            merged[key] = item[key]
        if canonical_changed:
            aliases = set(old.get("aliases", []))
            aliases.add(item["repo"])
            merged["aliases"] = sorted(aliases, key=str.lower)
        else:
            merged["repo"] = item["repo"]
            merged["url"] = item["url"]
        merged["status"] = old.get("status", item["status"])
        reconciled.append(merged)

    return {
        "schema": current.get("schema", "ger1e-security-catalog/v1"),
        "generated_from": [src["id"] for src in SOURCE_FILES],
        "last_verified": current.get("last_verified"),
        "repositories": sorted(reconciled, key=lambda x: (x["category"], x["repo"].lower())),
    }


def render_catalog(catalog: dict) -> str:
    groups = defaultdict(list)
    for item in catalog.get("repositories", []):
        groups[item["category"]].append(item)
    lines = [
        "### Security repository catalog",
        "",
        "Generated from `catalog/repos.yaml`. Do not hand-edit this file.",
        "",
        f"**Repositories:** {len(catalog.get('repositories', []))}",
        f"**Last verified:** {catalog.get('last_verified') or 'not yet verified'}",
        "",
        "Legend: `OFFICIAL/CANONICAL/COMMUNITY/LEGACY/TRAINING-LAB` · `SAFE-REFERENCE/ACTIVE-SECURITY-TOOL/OFFENSIVE-DUAL-USE/LIVE-MALWARE/VULNERABLE-LAB`.",
        "",
    ]
    for category in sorted(groups):
        lines += [f"#### {category.replace('-', ' ').title()}", ""]
        for item in sorted(groups[category], key=lambda x: x["repo"].lower()):
            meta = f"`{item['provenance']}` · `{item['risk']}` · `{item['status']}`"
            desc = f" — {item['description']}" if item.get("description") else ""
            aliases = f" · aliases: {', '.join(item['aliases'])}" if item.get("aliases") else ""
            lines.append(f"- [{item['repo']}]({item['url']}) — {meta}{aliases}{desc}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def validate_provider_catalog(catalog: dict):
    errors = []
    seen = set()
    for i, item in enumerate(catalog.get("providers", []), start=1):
        provider_id = item.get("id", "")
        if not provider_id:
            errors.append(f"missing provider id at entry {i}")
            continue
        if provider_id in seen:
            errors.append(f"duplicate provider id: {provider_id}")
        seen.add(provider_id)
        if slugify(provider_id) != provider_id:
            errors.append(f"provider id must be slugified: {provider_id}")
        if item.get("auth") not in VALID_PROVIDER_AUTH:
            errors.append(f"invalid provider auth at entry {i}: {item.get('auth')}")
        if item.get("access") not in VALID_PROVIDER_ACCESS:
            errors.append(f"invalid provider access at entry {i}: {item.get('access')}")
        if item.get("provenance") not in VALID_PROVIDER_PROVENANCE:
            errors.append(f"invalid provider provenance at entry {i}: {item.get('provenance')}")
        for field in ("api_base_url", "docs_url"):
            value = item.get(field)
            if value is not None and not value.startswith("https://"):
                errors.append(f"{field} must be https or null for {provider_id}")
        env_var = item.get("env_var")
        if env_var and not re.fullmatch(r"[A-Z][A-Z0-9_]*", env_var):
            errors.append(f"invalid env_var for {provider_id}: {env_var}")
        if not isinstance(item.get("capabilities", []), list):
            errors.append(f"capabilities must be a list for {provider_id}")
    return errors


def render_provider_catalog(catalog: dict) -> str:
    groups = defaultdict(list)
    for item in catalog.get("providers", []):
        groups[item.get("role", "uncategorized")].append(item)
    lines = [
        "### API / intelligence provider registry",
        "",
        "Generated from `catalog/providers.yaml`. Provider metadata is kept separate from GitHub repository provenance.",
        "",
        f"**Providers:** {len(catalog.get('providers', []))}",
        f"**Last verified:** {catalog.get('last_verified') or 'not yet verified'}",
        "",
    ]
    for role in sorted(groups):
        lines += [f"#### {role.replace('-', ' ').title()}", ""]
        for item in sorted(groups[role], key=lambda x: x["name"].lower()):
            lines.append(f"##### {item['name']}")
            lines.append(f"- API: {item.get('api_base_url') or 'not separately published'}")
            lines.append(f"- Docs: {item.get('docs_url') or 'not separately published'}")
            lines.append(f"- Auth: `{item['auth']}`" + (f" · env `{item['env_var']}`" if item.get("env_var") else ""))
            lines.append(f"- Access: `{item['access']}` · provenance `{item['provenance']}`")
            capabilities = ", ".join(item.get("capabilities", []))
            if capabilities:
                lines.append(f"- Capabilities: {capabilities}")
            if item.get("official_repositories"):
                lines.append("- Official repos: " + ", ".join(item["official_repositories"]))
            if item.get("community_integrations"):
                lines.append("- Verified integrations: " + ", ".join(item["community_integrations"]))
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def github_repo_state(repo: str, token: str | None):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ger1e-security-catalog",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
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
    return {
        "status": status,
        "full_name": data.get("full_name") or repo,
        "default_branch": data.get("default_branch"),
        "archived": bool(data.get("archived")),
        "html_url": data.get("html_url"),
    }


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
    lines = [
        "### Repository health",
        "",
        f"**Atlas verification:** {date}",
        f"**Repositories checked:** {len(checked)}",
        f"**Healthy:** {counts['ACTIVE']}",
        f"**Archived:** {counts['ARCHIVED']}",
        f"**Missing:** {counts['MISSING']}",
        f"**Private:** {counts['PRIVATE']}",
        "",
        "Generated by `tools/catalog.py`. Exact star counts are intentionally excluded.",
        "",
    ]
    exceptions = [r for r in checked if r["status"] != "ACTIVE"]
    if exceptions:
        lines += ["#### Exceptions", ""]
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
    blank = {"schema": "ger1e-security-catalog/v1", "last_verified": None, "repositories": []}
    catalog = reconcile_catalog(root, blank)
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.write:
        write_catalog(Path(args.catalog), catalog)
        print(f"bootstrapped {len(catalog['repositories'])} repositories")
    else:
        print(json.dumps(catalog, indent=2, ensure_ascii=False))
    return 0


def cmd_reconcile(args):
    root = Path(args.root)
    path = Path(args.catalog)
    current = load_catalog(path)
    catalog = reconcile_catalog(root, current)
    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    changed = catalog != current
    if args.write and changed:
        write_catalog(path, catalog)
    print(f"reconciled {len(catalog['repositories'])} repositories; changed={str(changed).lower()}")
    return 0


def cmd_providers_validate(args):
    catalog = load_catalog(Path(args.catalog))
    errors = validate_provider_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"provider catalog valid: {len(catalog.get('providers', []))} providers")
    return 0


def cmd_providers_build(args):
    catalog = load_catalog(Path(args.catalog))
    errors = validate_provider_catalog(catalog)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    Path(args.output).write_text(render_provider_catalog(catalog), encoding="utf-8")
    print(f"wrote {args.output}")
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
    parser = argparse.ArgumentParser(description="Maintain the ger1e security repository and provider catalogs")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("validate"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.set_defaults(func=cmd_validate)
    p = sub.add_parser("build"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--output", default="CATALOG.md"); p.set_defaults(func=cmd_build)
    p = sub.add_parser("bootstrap"); p.add_argument("--root", default="."); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--write", action="store_true"); p.set_defaults(func=cmd_bootstrap)
    p = sub.add_parser("reconcile"); p.add_argument("--root", default="."); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--write", action="store_true"); p.set_defaults(func=cmd_reconcile)
    p = sub.add_parser("providers-validate"); p.add_argument("--catalog", default="catalog/providers.yaml"); p.set_defaults(func=cmd_providers_validate)
    p = sub.add_parser("providers-build"); p.add_argument("--catalog", default="catalog/providers.yaml"); p.add_argument("--output", default="PROVIDERS.md"); p.set_defaults(func=cmd_providers_build)
    p = sub.add_parser("health"); p.add_argument("--catalog", default="catalog/repos.yaml"); p.add_argument("--report", default="LAST-VERIFIED.md"); p.add_argument("--token"); p.add_argument("--write", action="store_true"); p.set_defaults(func=cmd_health)
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
