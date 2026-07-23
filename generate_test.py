import os
import re
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
BASE_PATH = r"C:\Dev Projects 2026 [Local]\GIT\ai_qa_framework"


def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f: return f.read()
    return ""


def get_pom_references():
    pages_dir = os.path.join(BASE_PATH, "src", "pages")
    reference_string = "Available Page Objects and Methods:\n"
    if os.path.exists(pages_dir):
        for file in os.listdir(pages_dir):
            if file.endswith(".py") and not file.startswith("__"):
                content = read_file(os.path.join(pages_dir, file))
                structure = "\n".join(
                    [line.strip() for line in content.splitlines() if "class " in line or "def " in line])
                reference_string += f"\n--- File: {file} ---\n{structure}\n"
    return reference_string


def build_final_script(issue_id, raw_ai_output):
    """Extracts only the code steps from the AI and wraps them securely."""
    if "```python" in raw_ai_output:
        code = re.search(r"```python(.*?)```", raw_ai_output, re.DOTALL).group(1).strip()
    elif "```" in raw_ai_output:
        code = re.search(r"```(.*?)```", raw_ai_output, re.DOTALL).group(1).strip()
    else:
        code = raw_ai_output

    clean_body_lines = []
    for line in code.splitlines():
        stripped = line.strip()
        if not stripped or any(
                stripped.startswith(x) for x in ["def test_", "import ", "from ", "with sync_playwright"]):
            continue

        # --- PLAYWRIGHT METHOD SANITISER ---
        # Automatically converts hallucinated page.navigate() calls to valid page.goto()
        if "page.navigate(" in stripped:
            stripped = stripped.replace("page.navigate(", "page.goto(")

        clean_body_lines.append(stripped)

    indented_body = "\n".join([f"            {line}" for line in clean_body_lines])
    safe_func_id = issue_id.lower().replace("-", "_")

    return f"""from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage
# End of automated imports

def test_{safe_func_id}():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        try:
{indented_body}
            print("🚀 Test executed successfully!")
        finally:
            context.close()
            browser.close()
"""


def generate_test_case(issue_id):
    main_skill = read_file(os.path.join(BASE_PATH, "context_store", "global_domain_rules.md"))
    child_skill = read_file(
        os.path.join(BASE_PATH, "context_store", "child_contexts", f"{issue_id.upper().strip()}_ac.md"))
    pom_reference = get_pom_references()

    system_prompt = f"""
    You are an expert QA Engineer writing browser test steps for Playwright.
    Rules: {main_skill}
    Criteria: {child_skill}
    POM Layout: {pom_reference}

    Write ONLY the clean python code steps inside the test body. Assume a variable named `page` is active.
    Do NOT write a function definition (`def`), do NOT import anything, and do NOT include conversational text.
    """
    payload = {"model": "qwen2.5:7b", "prompt": system_prompt, "stream": False}
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        if response.status_code == 200:
            final_code = build_final_script(issue_id, response.json().get("response", ""))
            pending_dir = os.path.join(BASE_PATH, "tests", "pending_review")
            os.makedirs(pending_dir, exist_ok=True)
            pending_path = os.path.join(pending_dir, f"test_{issue_id.lower().replace('-', '_')}.py")
            with open(pending_path, "w", encoding="utf-8") as f: f.write(final_code)
            return pending_path
    except Exception as e:
        print(f"❌ Generation failure: {e}")
    return None
