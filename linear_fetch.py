import os
import re
import requests

# The official, documented Linear GraphQL endpoint
LINEAR_API_URL = "https://api.linear.app/graphql"
BASE_DIR = r"C:\Dev Projects 2026 Local\GIT\ai_qa_framework"



def get_raw_env_key():
    """Reads the .env file directly as raw text to prevent token truncation on Windows."""
    env_path = os.path.join(BASE_DIR, ".env")
    if not os.path.exists(env_path):
        return None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("LINEAR_API_KEY="):
                raw_val = line.split("=", 1)[1].strip()
                return raw_val.strip('"').strip("'")
    return None


def fetch_linear_issue(issue_id):
    linear_key = get_raw_env_key()
    if not linear_key:
        print("❌ Error: missing required string LINEAR_API_KEY inside your .env file.")
        return None

    # Mirroring your working Git script's header mapping exactly
    headers = {
        "Authorization": linear_key,
        "Content-Type": "application/json"
    }

    # Decoupling variables into JSON mapping to fulfill strict server criteria
    query = """
    query GetIssueDetails($id: String!) {
      issue(id: $id) {
        identifier
        title
        description
      }
    }
    """
    variables = {"id": issue_id.upper().strip()}

    try:
        resp = requests.post(
            LINEAR_API_URL,
            json={"query": query, "variables": variables},
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        if "errors" in data:
            print(f"❌ Linear API error: {data['errors']}")
            return None
        return data.get("data", {}).get("issue", None)
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None


def save_ac_context(issue_id):
    print(f"📡 Synchronizing with Linear Board for issue target: {issue_id}...")
    issue = fetch_linear_issue(issue_id)
    if not issue:
        print(f"❌ Issue data fetch returned empty result for {issue_id}.")
        return False

    body = issue.get('description', '')
    if not body:
        print(f"⚠️ Ticket description payload body is completely empty.")
        return False

    match = re.search(r'(?i)A\.C:?\s*(.*)', body, re.DOTALL)
    if match:
        ac_content = match.group(1).strip()
        output_dir = os.path.join(BASE_DIR, "context_store", "child_contexts")
        os.makedirs(output_dir, exist_ok=True)

        file_path = os.path.join(output_dir, f"{issue_id.upper().strip()}_ac.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(ac_content)
        print(f"🎯 Live Acceptance Criteria stored successfully: {file_path}")
        return True
    print(f"⚠️ Marker 'A.C:' not found inside the description of {issue_id}.")
    return False
