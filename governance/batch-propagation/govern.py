#!/usr/bin/env python3
"""Governance propagation script for hummbl-dev greenfield repos.

B0 dry-run factory: checks each repo for missing governance files,
maps from canonical templates, and produces a reviewable report.

Usage:
    python govern.py --dry-run              # default, safe
    python govern.py --check <repo-name>    # single repo check
    python govern.py --report <path>        # custom report path

Constraints:
- Default mode is --dry-run. No mutations without explicit --apply.
- Never overwrites existing files.
- Never creates PRs or commits.
- Only governance files: LICENSE, SECURITY, CODEOWNERS, CONTRIBUTING,
  AGENTS.md, .github/ISSUE_TEMPLATE/*, .github/PULL_REQUEST_TEMPLATE.md
- Treats existing files as authoritative.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPT_DIR / "templates"
MANIFEST_PATH = SCRIPT_DIR / "manifest.json"

# Canonical governance file paths relative to repo root
GOVERNANCE_FILES = [
    "LICENSE",
    "SECURITY.md",
    "CODEOWNERS",
    "CONTRIBUTING.md",
    "AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/ISSUE_TEMPLATE/content-correction.md",
]

# Files that are optional per repo type (e.g., AGENTS.md may not fit all repos)
OPTIONAL_FILES = ["AGENTS.md"]


@dataclass
class RepoCheck:
    name: str
    visibility: str
    tier: str
    impact: str
    disk_kb: int
    exists_on_remote: bool = False
    files_present: list[str] = field(default_factory=list)
    files_missing: list[str] = field(default_factory=list)
    files_flagged: list[str] = field(default_factory=list)
    status: str = "unknown"
    note: str = ""


def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_repo_exists(repo_name: str) -> bool:
    """Check if a repo exists in hummbl-dev org via gh CLI."""
    result = subprocess.run(
        ["gh", "repo", "view", f"hummbl-dev/{repo_name}", "--json", "name"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def list_repo_files(repo_name: str) -> list[str]:
    """List root-level files in a repo via gh CLI."""
    result = subprocess.run(
        ["gh", "api", f"/repos/hummbl-dev/{repo_name}/contents/", "--jq", ".[].path"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def list_repo_dotgithub_files(repo_name: str) -> list[str]:
    """List .github/ contents in a repo via gh CLI."""
    result = subprocess.run(
        ["gh", "api", f"/repos/hummbl-dev/{repo_name}/contents/.github", "--jq", ".[].path"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check_repo(repo_name: str, visibility: str, tier: str, impact: str, disk_kb: int) -> RepoCheck:
    """Check a single repo for governance file presence."""
    check = RepoCheck(
        name=repo_name,
        visibility=visibility,
        tier=tier,
        impact=impact,
        disk_kb=disk_kb,
    )

    if not check_repo_exists(repo_name):
        check.status = "missing"
        check.note = "Repo does not exist or is not accessible via gh CLI"
        return check

    check.exists_on_remote = True
    root_files = set(list_repo_files(repo_name))
    dotgithub_files = set(list_repo_dotgithub_files(repo_name))
    all_files = root_files | dotgithub_files

    for gf in GOVERNANCE_FILES:
        if gf in all_files:
            check.files_present.append(gf)
        elif gf in OPTIONAL_FILES:
            check.files_flagged.append(gf)
        else:
            check.files_missing.append(gf)

    if check.files_missing:
        check.status = "needs_governance"
        check.note = f"Missing {len(check.files_missing)} governance file(s)"
    elif check.files_flagged:
        check.status = "partial"
        check.note = f"Has all required; {len(check.files_flagged)} optional file(s) absent"
    else:
        check.status = "complete"
        check.note = "All governance files present"

    return check


def run_checks(manifest: dict, limit: Optional[list[str]] = None) -> list[RepoCheck]:
    """Run governance checks across all repos in manifest."""
    checks: list[RepoCheck] = []
    for repo in manifest["repos"]:
        name = repo["name"]
        if limit and name not in limit:
            continue
        print(f"Checking {name}...", file=sys.stderr)
        check = check_repo(
            name,
            visibility=repo["visibility"],
            tier=repo["tier"],
            impact=repo["impact"],
            disk_kb=repo["disk_kb"],
        )
        checks.append(check)
    return checks


def format_report(checks: list[RepoCheck], dry_run: bool = True) -> str:
    """Generate a human-readable dry-run report."""
    lines = []
    lines.append("# Governance Propagation Report")
    lines.append(f"**Mode**: {'DRY-RUN' if dry_run else 'LIVE'}")
    lines.append(f"**Date**: 2026-06-20")
    lines.append(f"**Scope**: hummbl-dev greenfield + near-greenfield repos")
    lines.append(f"**Total repos checked**: {len(checks)}")
    lines.append("")

    # Summary table
    status_counts: dict[str, int] = {}
    for c in checks:
        status_counts[c.status] = status_counts.get(c.status, 0) + 1

    lines.append("## Summary")
    lines.append("")
    for status, count in sorted(status_counts.items()):
        lines.append(f"- **{status}**: {count} repo(s)")
    lines.append("")

    # By impact
    lines.append("## By Impact (High → Low)")
    lines.append("")
    for impact in ["high", "medium", "low"]:
        impact_repos = [c for c in checks if c.impact == impact]
        if not impact_repos:
            continue
        lines.append(f"### {impact.upper()}")
        lines.append("")
        for c in sorted(impact_repos, key=lambda x: x.disk_kb):
            emoji = {"complete": "✅", "partial": "⚠️", "needs_governance": "❌", "missing": "❓"}.get(c.status, "❓")
            lines.append(f"- {emoji} **{c.name}** ({c.visibility}, {c.tier}, {c.disk_kb} KB) — {c.status}: {c.note}")
            if c.files_missing:
                for f in c.files_missing:
                    lines.append(f"  - Would add: `{f}`")
            if c.files_flagged:
                for f in c.files_flagged:
                    lines.append(f"  - Optional missing: `{f}`")
        lines.append("")

    # Detailed breakdown
    lines.append("## Detailed Breakdown")
    lines.append("")
    for c in sorted(checks, key=lambda x: (x.impact != "high", x.impact != "medium", x.name)):
        lines.append(f"### {c.name}")
        lines.append(f"- **Status**: {c.status}")
        lines.append(f"- **Visibility**: {c.visibility}")
        lines.append(f"- **Tier**: {c.tier}")
        lines.append(f"- **Impact**: {c.impact}")
        lines.append(f"- **Disk**: {c.disk_kb} KB")
        lines.append(f"- **Note**: {c.note}")
        if c.files_present:
            lines.append(f"- **Present**: {', '.join(f'`{f}`' for f in c.files_present)}")
        if c.files_missing:
            lines.append(f"- **Missing**: {', '.join(f'`{f}`' for f in c.files_missing)}")
        if c.files_flagged:
            lines.append(f"- **Optional absent**: {', '.join(f'`{f}`' for f in c.files_flagged)}")
        lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Governance propagation dry-run factory")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview changes without applying (default)")
    parser.add_argument("--apply", action="store_true", help="APPLY CHANGES — requires explicit confirmation")
    parser.add_argument("--check", type=str, help="Check a single repo by name")
    parser.add_argument("--report", type=str, default="reports/dry-run-report.md", help="Report output path")
    parser.add_argument("--manifest", type=str, default=str(MANIFEST_PATH), help="Manifest JSON path")
    args = parser.parse_args(argv)

    if args.apply:
        print("ERROR: --apply is not implemented in B0. This script is dry-run only.", file=sys.stderr)
        print("To apply changes, use the generated report to guide manual or scripted application.", file=sys.stderr)
        return 1

    manifest = load_manifest(Path(args.manifest))
    limit = [args.check] if args.check else None

    checks = run_checks(manifest, limit=limit)

    report_md = format_report(checks, dry_run=True)
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_md, encoding="utf-8")

    # Print concise summary to stdout
    needs = [c for c in checks if c.status == "needs_governance"]
    partial = [c for c in checks if c.status == "partial"]
    complete = [c for c in checks if c.status == "complete"]
    missing = [c for c in checks if c.status == "missing"]

    print(f"\n{'='*60}")
    print("GOVERNANCE PROPAGATION DRY-RUN SUMMARY")
    print(f"{'='*60}")
    print(f"Repos checked:        {len(checks)}")
    print(f"Needs governance:     {len(needs)}")
    print(f"Partial (optional):   {len(partial)}")
    print(f"Complete:             {len(complete)}")
    print(f"Missing/inaccessible: {len(missing)}")
    print(f"\nReport written to: {report_path}")

    if needs:
        print(f"\nRepos needing governance:")
        for c in needs:
            print(f"  - {c.name}: {', '.join(c.files_missing)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
