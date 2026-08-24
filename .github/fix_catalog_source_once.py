from pathlib import Path
import subprocess

path = Path("tools/catalog.py")
text = path.read_text(encoding="utf-8")
old = '    {"id": "soc-manual", "file": "SOC-MANUAL-REPOS.md"},\n'
if old not in text:
    raise SystemExit("stale SOC manual source reference not found")
path.write_text(text.replace(old, "", 1), encoding="utf-8")

subprocess.run(["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"], check=True)
subprocess.run(["python", "tools/catalog.py", "reconcile", "--write"], check=True)
subprocess.run(["python", "tools/catalog.py", "validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "build"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-build"], check=True)
