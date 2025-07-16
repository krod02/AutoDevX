import os
import json
import re
from github import Github
from dotenv import load_dotenv
from collections import defaultdict

# Load GitHub token
load_dotenv()
g = Github(os.getenv("GITHUB_TOKEN"))

# Expanded repos for greater dataset diversity
repos = [
    "tiangolo/fastapi",
    "PrefectHQ/prefect",
    "jina-ai/jina",
    "microsoft/semantic-kernel",
    "astral-sh/ruff",
    "open-metadata/OpenMetadata",
    "explosion/spaCy",
    "psf/requests",
    "encode/httpx",
    "streamlit/streamlit"
]

# Limits (balanced for rate limits)
MAX_PULLS = 1000
MAX_ISSUES = 1000

# Output dataset
output_data = []

for repo_name in repos:
    repo = g.get_repo(repo_name)
    print(f"\n📦 Scraping: {repo_name}")

    # Step 1: Build issue → PR map
    issue_to_prs = defaultdict(list)
    pr_metadata = defaultdict(list)

    for i, pr in enumerate(repo.get_pulls(state="closed")):
        if i >= MAX_PULLS:
            break
        if not pr.body:
            continue

        matches = re.findall(r"#(\d+)", pr.body)
        for match in matches:
            issue_num = int(match)
            issue_to_prs[issue_num].append(pr.html_url)
            pr_metadata[issue_num].append({
                "title": pr.title.strip(),
                "body": pr.body.strip() if pr.body else "",
                "url": pr.html_url
            })

    # Step 2: Loop through issues with adjusted filtering
    for i, issue in enumerate(repo.get_issues(state="closed")):
        if i >= MAX_ISSUES:
            break
        if issue.pull_request:
            continue

        issue_number = issue.number
        title_lower = issue.title.lower()

        # Adjusted filter: exclude questions or discussions but allow general feature/bugfix issues
        skip_keywords = ["how do i", "question", "help", "why", "error"]
        if any(k in title_lower for k in skip_keywords):
            continue

        if issue_number not in issue_to_prs:
            continue  # no matching PRs

        # Combine PR metadata into a 'plan'
        plan_chunks = []
        for pr in pr_metadata[issue_number]:
            plan_chunks.append(f"{pr['title']}\n\n{pr['body']}")
        plan_text = "\n---\n".join(plan_chunks)

        output_data.append({
            "input": f"{issue.title.strip()}\n\n{issue.body.strip() if issue.body else ''}",
            "plan": plan_text,
            "linked_prs": issue_to_prs[issue_number]
        })
        print(f"[+] Matched issue #{issue_number} to {len(issue_to_prs[issue_number])} PR(s)")

    print(f"🔎 Repo {repo_name} total matched examples: {len(output_data)}")

# Step 3: Save dataset
os.makedirs("data", exist_ok=True)
output_path = "data/planner_dataset.jsonl"
with open(output_path, "w", encoding="utf-8") as f:
    for row in output_data:
        json.dump(row, f)
        f.write("\n")

print(f"\n✅ Final saved dataset: {len(output_data)} examples → {output_path}")
