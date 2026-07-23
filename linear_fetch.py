import os
import re
import requests

LINEAR_API_URL = "https://linear.app"


def fetch_linear_issue(issue_id):
    # Retrieve the API Token dynamically from system environment or a text file
    token = os.getenv("LINEAR_API_TOKEN", "lin_api_Rnd3kKuWBS3bBGHMd1uOfCffuUHBPRqL9hiw6t0c")

    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }

    # GraphQL Query pulling identifier (e.g. QA-12) and description markdown block
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
        if 'errors' in data:
            raise Exception(f"Linear GraphQL Error: {data['errors']}")
        return data.get('data', {}).get('issue', None)
    else:
        raise Exception(f"Linear HTTP Communication Failure: {response.status_code}")


def save_ac_context(issue_id):
    issue = fetch_linear_issue(issue_id)
    if not issue or not issue.get('description'):
        print(f"❌ Issue '{issue_id}' not found or contains an empty description body.")
        return False

    body = issue['description']

    # Flexible multi-line matching targeting variants like 'A.C:', 'A.C', '## A.C:'
    match = re.search(r'(?i)A\.C:?\s*(.*)', body, re.DOTALL)

    if match:
        ac_content = match.group(1).strip()
        os.makedirs("context_store/child_contexts", exist_ok=True)
        file_path = f"context_store/child_contexts/{issue_id.upper()}_ac.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(ac_content)
        print(f"🎯 Live criteria synchronized and stored to: {file_path}")
        return True
    else:
        print(f"⚠️ Warning: Structural sequence 'A.C:' was not identified inside the markdown payload for {issue_id}.")
        return False
