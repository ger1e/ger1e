import subprocess

subprocess.run(["git", "checkout", "origin/main", "--", "catalog/repos.yaml"], check=True)
subprocess.run(["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"], check=True)
subprocess.run(["python", "tools/catalog.py", "reconcile"], check=True)
subprocess.run(["python", "tools/catalog.py", "validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "build"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-validate"], check=True)
subprocess.run(["python", "tools/catalog.py", "providers-build"], check=True)
