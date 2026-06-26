"""
One-command setup for Campus Placement System.
Run: python setup.py
"""
import subprocess
import sys
import os

def run(cmd, **kw):
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True, **kw)
    if result.returncode != 0:
        print(f"ERROR: command failed (exit code {result.returncode})")
        sys.exit(1)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("  Campus Placement System — Quick Setup")
print("=" * 50)

# 1. Install dependencies
run(f"{sys.executable} -m pip install -r requirements.txt")

# 2. Migrate database (creates db.sqlite3 automatically)
run(f"{sys.executable} manage.py migrate")

# 3. Seed skills
run(f"{sys.executable} manage.py seed_skills")

# 4. Create superuser
print("\n--- Create an admin login (for /admin/) ---")
run(f"{sys.executable} manage.py createsuperuser")

print("\n✅ Setup complete!")
print("   Run the server:  python manage.py runserver")
print("   Open browser:    http://127.0.0.1:8000/")
