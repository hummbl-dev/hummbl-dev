#!/usr/bin/env python3

"""Validate GitHub repository links in README.md.

Checks that every ``https://github.com/hummbl-dev/<repo>`` URL in README resolves
to live GitHub metadata and reports visibility/archival status.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
API_URL_TMPL = "https://api.github.com/repos/{owner}/{repo}"
REPO_LINK_RE = re.compile(
    r"\[[^\]]+\]\((https://github\.com/hummbl-dev/([A-Za-z0-9_.-]+)(?:/[^)]*)?)\)",
    re.IGNORECASE,
)


def check_repo(owner: str, repo: str, token: str | None) -> dict:
    """Return repository metadata from the GitHub API."""
    req = urllib.request.Request(API_URL_TMPL.format(owner=owner, repo=repo))
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "hummbl-dev-readme-link-check")
    if token:
        req.add_header("Authorization", f"token {token}")

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return {
            "repo": repo,
            "url": payload.get("html_url", API_URL_TMPL.format(owner=owner, repo=repo)),
            "exists": True,
            "archived": bool(payload.get("archived", False)),
            "private": bool(payload.get("private", False)),
            "status": "ok",
            "status_code": int(response.getcode()),
        }
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {
                "repo": repo,
                "url": API_URL_TMPL.format(owner=owner, repo=repo),
                "exists": False,
                "status": "missing",
                "status_code": exc.code,
            }
        if exc.code in (401, 403):
            return {
                "repo": repo,
                "url": API_URL_TMPL.format(owner=owner, repo=repo),
                "exists": None,
                "status": "auth-required-or-rate-limited",
                "status_code": exc.code,
            }
        return {
            "repo": repo,
            "url": API_URL_TMPL.format(owner=owner, repo=repo),
            "exists": None,
            "status": f"http-{exc.code}",
            "status_code": exc.code,
        }
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return {
            "repo": repo,
            "url": API_URL_TMPL.format(owner=owner, repo=repo),
            "exists": None,
            "status": "network-error",
            "error": str(exc),
        }


def extract_repo_links(readme_text: str) -> list[tuple[str, str]]:
    """Return (label, repo) pairs for markdown links to hummbl-dev repos."""
    seen = {}
    for match in REPO_LINK_RE.finditer(readme_text):
        repo = match.group(1).split("/")[-1]
        label = match.group(0).split("]")[0][1:]
        seen.setdefault(repo, label)
    return [(label, repo) for repo, label in seen.items()]


def main() -> int:
    if not README_PATH.exists():
        print(f"README not found: {README_PATH}")
        return 2

    content = README_PATH.read_text(encoding="utf-8")
    links = extract_repo_links(content)
    if not links:
        print("No markdown GitHub repo links found in README.md")
        return 0

    token = os.getenv("GITHUB_TOKEN")
    owner = "hummbl-dev"
    has_errors = False

    print("repo-link-check: summary")
    print("repo | status | details")
    print("-----|--------|--------")

    for label, repo in links:
        result = check_repo(owner, repo, token)
        status = result["status"]
        if status == "ok":
            vis = "private" if result["private"] else "public"
            stage = "archived" if result["archived"] else "active"
            print(f"{label} -> {repo} | OK {status} ({vis}, {stage}) | {result['url']}")
            continue

        if status == "missing":
            has_errors = True
            print(f"{label} -> {repo} | ERROR {status} | {result['url']}")
            continue

        print(f"{label} -> {repo} | WARN {status} | {result['url']}")

    if has_errors:
        print("\nValidation failed: one or more linked repositories are missing.")
        return 1

    print("\nValidation passed: all linked repositories resolve in GitHub metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
