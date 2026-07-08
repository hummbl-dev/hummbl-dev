#!/usr/bin/env python3
"""
Safe PR creation helper — verifies branch before creating PR.

Usage:
    python scripts/safe_pr_create.py <branch> <title> [--body-file <file>]

This prevents the error where gh pr create attaches to the wrong branch
because the working tree was on a different branch than intended.
"""
import subprocess, sys, argparse

def main():
    parser = argparse.ArgumentParser(description="Safe PR creation with branch verification")
    parser.add_argument("branch", help="Branch to create PR from")
    parser.add_argument("title", help="PR title")
    parser.add_argument("--body-file", help="Path to PR body file")
    args = parser.parse_args()

    # Verify current branch
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True,
        check=True
    )
    current_branch = result.stdout.strip()

    if current_branch != args.branch:
        print(f"ERROR: Current branch is '{current_branch}', expected '{args.branch}'", file=sys.stderr)
        print(f"Run: git checkout {args.branch}", file=sys.stderr)
        sys.exit(1)

    print(f"Verified: on branch {args.branch}")

    # Build gh pr create command
    cmd = ["gh", "pr", "create", "--title", args.title]
    if args.body_file:
        cmd.extend(["--body-file", args.body_file])

    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
