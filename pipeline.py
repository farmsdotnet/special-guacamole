import os
import shutil
import requests
from linear_fetch import save_ac_context
from generate_test import generate_test_case, read_file, get_pom_references, build_final_script, OLLAMA_URL


def regenerate_with_feedback(issue_id, feedback_text, current_code):
    main_skill = read_file("context_store/global_domain_rules.md")
    child_skill = read_file(f"context_store/child_contexts/{issue_id}_ac.md")
    pom_reference = get_pom_references()

    refinement_prompt = f"""
    Modify these Playwright test steps based on user feedback.
    Criteria: {child_skill}
    Previous Output: {current_code}

    HUMAN FEEDBACK TO APPLY: {feedback_text}

    Write ONLY the clean python code steps. Do NOT write a function definition (`def`) or any imports.
    """
    payload = {"model": "qwen2.5:7b", "prompt": refinement_prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    if response.status_code == 200:
        return build_final_script(issue_id, response.json().get("response", ""))
    raise Exception("Local model disconnected.")


def run_pipeline(issue_id):
    safe_id = issue_id.lower().replace('-', '_')
    if issue_id.upper() != "TKT-999":
        if not save_ac_context(issue_id):
            print(f"❌ Aborting. Could not sync criteria for {issue_id}")
            return

    pending_file = generate_test_case(issue_id)
    if not pending_file:
        print("❌ Generation failed. No script was compiled.")
        return

    while True:
        print(f"\n==================== [REVIEWING]: {pending_file} ====================")
        print(read_file(pending_file))
        print("=====================================================================")

        choice = input("\nSelect Action -> [A]pprove | [D]ecline | [S]uggest Changes: ").strip().lower()

        if choice == 'a':
            os.makedirs("tests/staging", exist_ok=True)
            dest = f"tests/staging/test_{safe_id}.py"
            if os.path.exists(dest): os.remove(dest)
            shutil.move(pending_file, dest)
            print(f"🚀 Approved! Saved to live suite: {dest}")
            break
        elif choice in ['d', 'r', 'decline']:
            if os.path.exists(pending_file): os.remove(pending_file)
            print("🗑️ Script declined and deleted.")
            break
        elif choice == 's':
            feedback = input("\n📝 Enter adjustments for the AI: ").strip()
            if feedback:
                try:
                    updated_code = regenerate_with_feedback(issue_id, feedback, read_file(pending_file))
                    with open(pending_file, "w", encoding="utf-8") as f:
                        f.write(updated_code)
                except Exception as e:
                    print(f"❌ Refinement failed: {e}")


if __name__ == "__main__":
    ticket = input("Enter Linear Ticket ID to process (or 'TKT-999' for control test): ").strip()
    if ticket:
        run_pipeline(ticket)
