import os
import re
import requests

LINEAR_API_URL = "https://linear.app"
# Replace with your actual token or set it in your environment variables
LINEAR_TOKEN = os.getenv("LINEAR_API_TOKEN", "your_linear_api_token_here")


def fetch_linear_issue(issue_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": LINEAR_TOKEN
    }
    # GraphQL Query to pull the issue description
    query = """
    query {
      issue(id: "%s") {
        identifier
        description
      }
    }
    """ % issue_id

    response = requests.post(LINEAR_API_URL, json={'query': query}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['issue']
    else:
        raise Exception(f"Linear API error: {response.status_code}")


def save_ac_context(issue_id):
    issue = fetch_linear_issue(issue_id)
    if not issue or not issue.get('description'):
        print(f"❌ No description found for {issue_id}")
        return False

    body = issue['description']

    # Matches 'A.C:' case-insensitive and grabs all text following it
    match = re.search(r'(?i)A\.C:\s*(.*)', body, re.DOTALL)

    if match:
        ac_content = match.group(1).strip()
        os.makedirs("context_store/child_contexts", exist_ok=True)
        file_path = f"context_store/child_contexts/{issue_id}_ac.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(ac_content)
        print(f"✅ Context saved: {file_path}")
        return True
    else:
        print(f"⚠️ Marker 'A.C:' not found in issue {issue_id}")
        return False


if __name__ == "__main__":
    # Test execution with a dummy/real ticket ID
    # save_ac_context("TKT-101")
    pass
