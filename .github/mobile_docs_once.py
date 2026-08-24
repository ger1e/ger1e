from pathlib import Path
import re
import subprocess

TARGETS = [
    Path("API-TOOLS-REPOS.md"),
    Path("SECURITY-REPOS.md"),
    Path("SECURITY.md"),
    Path("LAST-VERIFIED.md"),
    Path("docs/GITHUB-ACCOUNT-POLISH.md"),
    Path("docs/ecthp-asset-source.md"),
    Path("docs/maintenance-sync.md"),
    Path("lab/README.md"),
]

HEADING = re.compile(r"^(#{1,6})(\s+.*)$")

def compact(text: str) -> str:
    out = []
    in_fence = False
    fence = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = None
            out.append(line)
            continue
        if not in_fence:
            m = HEADING.match(line.rstrip("\r\n"))
            if m:
                level = min(len(m.group(1)) + 2, 6)
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                line = "#" * level + m.group(2) + ending
        out.append(line)
    return "".join(out)

for path in TARGETS:
    original = path.read_text(encoding="utf-8")
    updated = compact(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")

catalog_path = Path("tools/catalog.py")
catalog = catalog_path.read_text(encoding="utf-8")
replacements = [
    ('if line.startswith("## "):\n            category = slugify(line[3:].strip())', 'if line.startswith("#### "):\n            category = slugify(line[5:].strip())'),
    ('"# Security repository catalog"', '"### Security repository catalog"'),
    ('lines += [f"## {category.replace(\'-\', \' \').title()}", ""]', 'lines += [f"#### {category.replace(\'-\', \' \').title()}", ""]'),
    ('"# API / intelligence provider registry"', '"### API / intelligence provider registry"'),
    ('lines += [f"## {role.replace(\'-\', \' \').title()}", ""]', 'lines += [f"#### {role.replace(\'-\', \' \').title()}", ""]'),
    ('lines.append(f"### {item[\'name\']}")', 'lines.append(f"##### {item[\'name\']}")'),
    ('"# Repository health"', '"### Repository health"'),
    ('lines += ["## Exceptions", ""]', 'lines += ["#### Exceptions", ""]'),
]
for old, new in replacements:
    if old not in catalog:
        raise SystemExit(f"expected catalog renderer token not found: {old}")
    catalog = catalog.replace(old, new, 1)
catalog_path.write_text(catalog, encoding="utf-8")

subprocess.run(["python", "tools/catalog.py", "validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "build"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-build"], check=True)
