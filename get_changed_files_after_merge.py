import subprocess
import sys
import os

def run_cmd(cmd):
    """Run a shell command safely and return its output."""
    try:
        result = subprocess.run(
            cmd, shell=True, text=True, capture_output=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Command failed: {cmd}\n{e.stderr}")
        sys.exit(1)

def ensure_repo():
    """Ensure current folder is a Git repo."""
    if not os.path.exists(".git"):
        print("❌ This folder is not a Git repository. Please run this script inside your repo.")
        sys.exit(1)

def update_main_branch():
    """Switch to main branch and pull the latest changes."""
    print("🔄 Updating local main branch...")
    run_cmd("git fetch origin")
    run_cmd("git checkout main")
    run_cmd("git pull origin main")
    print("✅ Main branch updated.\n")

def get_all_commits():
    """Get all commits (including merges) from main branch."""
    print("📜 Collecting all commits from main branch...")
    log_output = run_cmd("git log --oneline main")
    commits = [line.split()[0] for line in log_output.splitlines() if line.strip()]
    return commits

def get_changed_files(commit_id):
    """List all files changed in a given commit."""
    files_output = run_cmd(f"git show --name-only --pretty=format: {commit_id}")
    return [f for f in files_output.splitlines() if f.strip()]

def main():
    ensure_repo()
    update_main_branch()

    commits = get_all_commits()
    if not commits:
        print("⚠️ No commits found in main branch.")
        return

    print("🔍 Listing files changed in each commit (including merges):\n")
    for commit in commits:
        print(f"\n📦 Commit: {commit}")
        files = get_changed_files(commit)
        if files:
            for file in files:
                print(f"  • {file}")
        else:
            print("  (No file changes in this commit)")

    print("\n✅ Completed — all changed files in main branch have been listed.")

if __name__ == "__main__":
    main()
