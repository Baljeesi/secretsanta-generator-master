import subprocess
import sys
import os
import csv
from datetime import datetime, timedelta

def run_cmd(cmd):
    """Run shell command safely and return its output."""
    try:
        result = subprocess.run(
            cmd, shell=True, text=True, capture_output=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Command failed: {cmd}\n{e.stderr}")
        sys.exit(1)

def ensure_repo():
    """Ensure script runs inside a Git repository."""
    if not os.path.exists(".git"):
        print("❌ Not a Git repositor
