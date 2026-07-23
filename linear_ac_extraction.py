# snippet for parsing linear body
import re

def extract_ac(ticket_body, ticket_id):
    # Matches 'A.C:' case-insensitive and grabs all text following it
    match = re.search(r'(?i)A\.C:\s*(.*)', ticket_body, re.DOTALL)
    if match:
        ac_content = match.group(1).strip()
        with open(f"context_store/child_contexts/{ticket_id}_ac.md", "w") as f:
            f.write(ac_content)
