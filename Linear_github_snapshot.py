#!/usr/bin/env python3
"""
linear_github_snapshot.py

***MADE SOME SAMPLE TEXT HERE TO PUSH TO TEST BRANCH ['far-5']  ****

Lightweight CLI that cross-checks Linear tickets (issues) belonging to a given
Project against the commits present on a given GitHub branch, and writes the
result to a snapshot.md file. Optionally narrows to a single Project
Milestone (Linear's concept for a release/checkpoint within a project).

A ticket counts as "found" on the branch if its Linear identifier (e.g.
"ENG-123") appears either:
  - anywhere in a commit's message, or
  - in the source branch name of a merge commit (e.g. "Merge pull request #12
    from your-org/eng-123-fix-thing")

Auth (env vars):
  LINEAR_API_KEY   Linear personal API key
  GITHUB_TOKEN     GitHub personal access token (repo read scope)
  GITHUB_REPO      "owner/repo", e.g. "IQGeo/myworld-dev"

Usage:
  python linear_github_snapshot.py --branch v7.3 --project "Reporting Revamp"
  python linear_github_snapshot.py --branch main --project "Q3 Rollout" \
      --milestone "Release 1" --output out.md
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone

import requests

LINEAR_API_URL = "https://api.linear.app/graphql"
GITHUB_API_URL = "https://api.github.com"

MERGE_PR_RE = re.compile(r"Merge pull request #\d+ from [\w\-.]+/(?P<branch>[\w\-./]+)")
MERGE_BRANCH_RE = re.compile(r"Merge branch '(?P<branch>[^']+)'")


def die(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        die(f"missing required environment variable {name}")
    return value


# --------------------------------------------------------------------------
# Linear
# --------------------------------------------------------------------------

def linear_request(api_key: str, query: str, variables: dict) -> dict:
    resp = requests.post(
        LINEAR_API_URL,
        json={"query": query, "variables": variables},
        headers={"Authorization": api_key, "Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        die(f"Linear API error: {data['errors']}")
    return data["data"]


def find_project_id(api_key: str, project_name: str) -> str:
    query = """
    query ProjectByName($name: String!) {
      projects(filter: { name: { eqIgnoreCase: $name } }) {
        nodes { id name }
      }
    }
    """
    data = linear_request(api_key, query, {"name": project_name})
    nodes = data["projects"]["nodes"]
    if not nodes:
        die(f"no Linear project found with name '{project_name}'")
    if len(nodes) > 1:
        print(
            f"Warning: multiple projects matched '{project_name}', using the first one "
            f"({nodes[0]['name']})",
            file=sys.stderr,
        )
    return nodes[0]["id"]


def find_milestone_id(api_key: str, project_id: str, milestone_name: str) -> str:
    """Look up a Project Milestone (release checkpoint) by name within a project."""
    query = """
    query ProjectMilestones($projectId: String!) {
      project(id: $projectId) {
        projectMilestones {
          nodes { id name }
        }
      }
    }
    """
    data = linear_request(api_key, query, {"projectId": project_id})
    nodes = data["project"]["projectMilestones"]["nodes"]
    matches = [n for n in nodes if n["name"].lower() == milestone_name.lower()]
    if not matches:
        available = ", ".join(n["name"] for n in nodes) or "(none defined)"
        die(f"no milestone named '{milestone_name}' on this project. Available: {available}")
    return matches[0]["id"]


def get_issues_for_project(api_key: str, project_id: str, milestone_id: str = None) -> list:
    issue_filter = {"project": {"id": {"eq": project_id}}}
    if milestone_id:
        issue_filter["projectMilestone"] = {"id": {"eq": milestone_id}}

    query = """
    query IssuesByProject($filter: IssueFilter!, $after: String) {
      issues(
        filter: $filter
        first: 100
        after: $after
      ) {
        nodes {
          identifier
          title
          url
          state { name type }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
    """
    issues = []
    cursor = None
    while True:
        data = linear_request(api_key, query, {"filter": issue_filter, "after": cursor})
        block = data["issues"]
        issues.extend(block["nodes"])
        if not block["pageInfo"]["hasNextPage"]:
            break
        cursor = block["pageInfo"]["endCursor"]
    return issues


# --------------------------------------------------------------------------
# GitHub
# --------------------------------------------------------------------------

def get_branch_commits(token: str, repo: str, branch: str, max_commits: int) -> list:
    commits = []
    page = 1
    per_page = 100
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    while len(commits) < max_commits:
        resp = requests.get(
            f"{GITHUB_API_URL}/repos/{repo}/commits",
            params={"sha": branch, "per_page": per_page, "page": page},
            headers=headers,
            timeout=30,
        )
        if resp.status_code == 404:
            die(f"repo '{repo}' or branch '{branch}' not found on GitHub")
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        commits.extend(batch)
        if len(batch) < per_page:
            break
        page += 1
    return commits[:max_commits]


def extract_merge_branch(message: str) -> str:
    m = MERGE_PR_RE.search(message) or MERGE_BRANCH_RE.search(message)
    return m.group("branch") if m else ""


# --------------------------------------------------------------------------
# Matching
# --------------------------------------------------------------------------

def ticket_mentioned(identifier: str, message: str, merge_branch: str) -> bool:
    pattern = re.compile(re.escape(identifier), re.IGNORECASE)
    if pattern.search(message):
        return True
    if merge_branch and pattern.search(merge_branch):
        return True
    return False


def match_tickets_to_commits(issues: list, commits: list) -> dict:
    prepared = []
    for c in commits:
        message = c["commit"]["message"]
        prepared.append(
            {
                "sha": c["sha"],
                "short_sha": c["sha"][:7],
                "message": message.splitlines()[0] if message else "",
                "merge_branch": extract_merge_branch(message),
                "url": c["html_url"],
                "date": c["commit"]["committer"]["date"],
            }
        )

    matches = {}
    for issue in issues:
        identifier = issue["identifier"]
        found = [
            c for c in prepared
            if ticket_mentioned(identifier, c["message"], c["merge_branch"])
        ]
        matches[identifier] = found
    return matches


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def render_snapshot(project_name: str, milestone_name: str, repo: str, branch: str,
                     issues: list, matches: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Linear ↔ GitHub Snapshot",
        "",
        f"**Project:** {project_name}",
    ]
    if milestone_name:
        lines.append(f"**Milestone (release):** {milestone_name}")
    lines += [
        f"**Repository:** {repo}",
        f"**Branch:** {branch}",
        f"**Generated:** {now}",
        "",
        "## Ticket Status",
        "",
        "| Ticket | Title | Linear Status | Commits Found | Commit(s) |",
        "|---|---|---|---|---|",
    ]

    found_count = 0
    for issue in issues:
        identifier = issue["identifier"]
        title = issue["title"]
        state = issue["state"]["name"]
        commits = matches[identifier]
        if commits:
            found_count += 1
            shas = ", ".join(f"`{c['short_sha']}`" for c in commits)
        else:
            shas = "—"
        lines.append(
            f"| [{identifier}]({issue['url']}) | {title} | {state} | "
            f"{'✅' if commits else '❌'} {len(commits)} | {shas} |"
        )

    lines += ["", "## Commit Details", ""]
    for issue in issues:
        identifier = issue["identifier"]
        commits = matches[identifier]
        if not commits:
            continue
        lines.append(f"### {identifier} — {issue['title']}")
        for c in commits:
            lines.append(f"- `{c['short_sha']}` {c['message']} ({c['date']}) — [view]({c['url']})")
        lines.append("")

    total = len(issues)
    lines += [
        "## Summary",
        "",
        f"- {found_count} of {total} ticket(s) have at least one matching commit on `{branch}`",
        f"- {total - found_count} ticket(s) have no matching commits on `{branch}`",
    ]

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cross-check Linear tickets for a Project (optionally scoped to a Milestone/release) "
                    "against commits on a GitHub branch."
    )
    parser.add_argument("--branch", required=True, help="GitHub branch to check commits on")
    parser.add_argument("--project", required=True, help="Linear Project name")
    parser.add_argument(
        "--milestone",
        default=None,
        help="Optional Linear Project Milestone name (release checkpoint) to narrow tickets to",
    )
    parser.add_argument("--output", default="snapshot.md", help="Output markdown file (default: snapshot.md)")
    parser.add_argument("--max-commits", type=int, default=1000, help="Max commits to scan (default: 1000)")
    args = parser.parse_args()

    linear_key = require_env("LINEAR_API_KEY")
    github_token = require_env("GITHUB_TOKEN")
    repo = require_env("GITHUB_REPO")

    print(f"Looking up Linear project '{args.project}'...")
    project_id = find_project_id(linear_key, args.project)

    milestone_id = None
    if args.milestone:
        print(f"Looking up milestone '{args.milestone}'...")
        milestone_id = find_milestone_id(linear_key, project_id, args.milestone)

    print("Fetching issues...")
    issues = get_issues_for_project(linear_key, project_id, milestone_id)
    if not issues:
        die("no issues found for the given project/milestone")
    print(f"Found {len(issues)} ticket(s).")

    print(f"Fetching commits on '{args.branch}' in {repo}...")
    commits = get_branch_commits(github_token, repo, args.branch, args.max_commits)
    print(f"Fetched {len(commits)} commit(s).")

    matches = match_tickets_to_commits(issues, commits)

    report = render_snapshot(args.project, args.milestone, repo, args.branch, issues, matches)
    with open(args.output, "w") as f:
        f.write(report)

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()