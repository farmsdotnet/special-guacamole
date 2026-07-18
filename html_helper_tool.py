#!/usr/bin/env python3
"""
locator_finder.py — generate test-automation locators for a web page.

For a given URL (or local HTML file), this script:
  1. Fetches the page (optionally rendering JS first via Playwright).
  2. Finds elements that are commonly targeted in test automation
     (links, buttons, inputs, selects, textareas, forms, labels, and any
     element with a role / data-testid / onclick).
  3. Generates several independent locator strategies per element
     (ID, CSS selector, XPath, Name, Link Text, data-testid, aria-label,
     class-based CSS, and a structural fallback).
  4. Validates every locator against the parsed DOM and reports whether
     it matches exactly one element (safe to use) or several (ambiguous).
  5. Writes everything to a Markdown report.

Usage:
  python locator_finder.py https://example.com
  python locator_finder.py https://example.com -o report.md
  python locator_finder.py https://example.com --render        # render JS with Playwright first
  python locator_finder.py ./saved_page.html                   # works on local files too

Dependencies (all already common / lightweight):
  pip install requests beautifulsoup4 lxml
  # optional, only needed for --render:
  pip install playwright && playwright install chromium
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from lxml import etree, html as lxml_html


INTERACTIVE_TAGS = {"a", "button", "input", "select", "textarea", "form", "label", "option", "summary"}
TESTID_ATTRS = ("data-testid", "data-test", "data-cy", "data-qa")

# Lower number = higher priority / more recommended for automation.
PRIORITY = {
    "testid": 1,
    "id": 2,
    "name": 3,
    "aria-label": 4,
    "link-text": 5,
    "button-text": 5,
    "placeholder": 6,
    "class": 7,
    "structural": 8,
}

PRIORITY_LABEL = {
    1: "Recommended (test id)",
    2: "Recommended (id)",
    3: "Good (name)",
    4: "Good (aria-label)",
    5: "Good (visible text)",
    6: "OK (placeholder)",
    7: "Fallback (class)",
    8: "Fallback (structural / brittle)",
}


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------

def fetch_html(source, render=False, timeout=20):
    """Return raw HTML for a URL or local file path."""
    is_url = re.match(r"^https?://", source, re.I) is not None

    if not is_url:
        path = os.path.abspath(source)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Local file not found: {path}")
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

    if render:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            print(
                "[warn] --render requested but Playwright isn't installed. "
                "Falling back to a plain HTTP fetch (no JS execution).\n"
                "        Install with: pip install playwright && playwright install chromium",
                file=sys.stderr,
            )
            render = False

    if render:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(source, wait_until="networkidle", timeout=timeout * 1000)
            content = page.content()
            browser.close()
            return content

    headers = {"User-Agent": "Mozilla/5.0 (compatible; LocatorFinder/1.0)"}
    resp = requests.get(source, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text


# --------------------------------------------------------------------------
# Escaping helpers
# --------------------------------------------------------------------------

def css_escape(value):
    """Minimal escaping for values embedded in CSS attribute/class selectors."""
    return re.sub(r'(["\\])', r"\\\1", value)


def xpath_literal(value):
    """Return a safely quoted XPath string literal, handling embedded quotes."""
    if '"' not in value:
        return f'"{value}"'
    if "'" not in value:
        return f"'{value}'"
    parts = value.split('"')
    return "concat(" + ', \'"\', '.join(f'"{p}"' for p in parts) + ")"


def class_contains_xpath(tag_name, classes):
    conds = " and ".join(
        f'contains(concat(" ", normalize-space(@class), " "), " {c} ")' for c in classes
    )
    return f"//{tag_name}[{conds}]"


# --------------------------------------------------------------------------
# Element selection
# --------------------------------------------------------------------------

def is_testable(tag):
    if tag.name in INTERACTIVE_TAGS:
        return True
    if tag.has_attr("role"):
        return True
    if tag.has_attr("onclick"):
        return True
    for attr in TESTID_ATTRS:
        if tag.has_attr(attr):
            return True
    return False


CONTAINER_TAGS = {"form", "select", "div", "nav", "header", "footer", "section"}


def short_label(tag):
    """A human-readable label to identify the element in the report."""
    # For containers, prefer an attribute (id/name/aria-label) over concatenated
    # child text, since that text is noisy and not what identifies the element.
    if tag.name in CONTAINER_TAGS:
        for attr in ("aria-label", "id", "name"):
            if tag.has_attr(attr) and tag[attr].strip():
                return f'{attr}="{tag[attr].strip()[:50]}"'

    text = tag.get_text(" ", strip=True)
    if text:
        return text[:60]
    for attr in ("aria-label", "placeholder", "alt", "title", "name", "id"):
        if tag.has_attr(attr) and tag[attr].strip():
            return f'{attr}="{tag[attr].strip()[:50]}"'
    if tag.name == "input" and tag.has_attr("type"):
        return f'input[type={tag["type"]}]'
    return f"<{tag.name}> (no visible text)"


# --------------------------------------------------------------------------
# Locator generation
# --------------------------------------------------------------------------

def build_locators(tag):
    """
    Return a list of dicts: {strategy, value, priority, xpath_check}
    xpath_check is the XPath equivalent used purely to validate uniqueness,
    even for CSS-strategy locators.
    """
    name = tag.name
    locators = []

    def add(strategy, value, priority, xpath_check):
        locators.append(
            {"strategy": strategy, "value": value, "priority": priority, "xpath_check": xpath_check}
        )

    # 1. data-testid family (highest priority - stable, automation-only attributes)
    for attr in TESTID_ATTRS:
        if tag.has_attr(attr) and tag[attr].strip():
            val = tag[attr].strip()
            add("CSS", f'[{attr}="{val}"]', PRIORITY["testid"], f"//*[@{attr}={xpath_literal(val)}]")
            add("XPath", f"//{name}[@{attr}={xpath_literal(val)}]", PRIORITY["testid"],
                f"//{name}[@{attr}={xpath_literal(val)}]")

    # 2. ID
    if tag.has_attr("id") and tag["id"].strip():
        eid = tag["id"].strip()
        add("ID", eid, PRIORITY["id"], f'//*[@id={xpath_literal(eid)}]')
        add("CSS", f"#{css_escape(eid)}", PRIORITY["id"], f'//*[@id={xpath_literal(eid)}]')
        add("XPath", f"//{name}[@id={xpath_literal(eid)}]", PRIORITY["id"],
            f"//{name}[@id={xpath_literal(eid)}]")

    # 3. Name attribute
    if tag.has_attr("name") and tag["name"].strip():
        val = tag["name"].strip()
        add("Name", val, PRIORITY["name"], f"//{name}[@name={xpath_literal(val)}]")
        add("CSS", f'{name}[name="{val}"]', PRIORITY["name"], f"//{name}[@name={xpath_literal(val)}]")
        add("XPath", f"//{name}[@name={xpath_literal(val)}]", PRIORITY["name"],
            f"//{name}[@name={xpath_literal(val)}]")

    # 4. aria-label
    if tag.has_attr("aria-label") and tag["aria-label"].strip():
        val = tag["aria-label"].strip()
        add("CSS", f'{name}[aria-label="{val}"]', PRIORITY["aria-label"],
            f"//{name}[@aria-label={xpath_literal(val)}]")
        add("XPath", f"//{name}[@aria-label={xpath_literal(val)}]", PRIORITY["aria-label"],
            f"//{name}[@aria-label={xpath_literal(val)}]")

    # 5. Visible text (links / buttons)
    text = tag.get_text(" ", strip=True)
    if name == "a" and text:
        add("Link Text", text, PRIORITY["link-text"],
            f"//a[normalize-space(text())={xpath_literal(text)}]")
        add("XPath", f"//a[normalize-space(text())={xpath_literal(text)}]", PRIORITY["link-text"],
            f"//a[normalize-space(text())={xpath_literal(text)}]")
    elif name == "button" and text:
        add("XPath", f"//button[normalize-space(text())={xpath_literal(text)}]", PRIORITY["button-text"],
            f"//button[normalize-space(text())={xpath_literal(text)}]")

    # 6. Placeholder (inputs/textareas)
    if tag.has_attr("placeholder") and tag["placeholder"].strip():
        val = tag["placeholder"].strip()
        add("CSS", f'{name}[placeholder="{val}"]', PRIORITY["placeholder"],
            f"//{name}[@placeholder={xpath_literal(val)}]")
        add("XPath", f"//{name}[@placeholder={xpath_literal(val)}]", PRIORITY["placeholder"],
            f"//{name}[@placeholder={xpath_literal(val)}]")

    # 7. Class-based CSS (skip classes that look auto-generated / hashed)
    if tag.has_attr("class"):
        classes = [
            c for c in tag["class"]
            if c and not re.match(r"^[a-zA-Z]{0,3}-?[0-9a-f]{6,}$", c) and not re.match(r"^css-", c)
        ]
        if classes:
            classes = classes[:3]
            css_sel = name + "".join(f".{css_escape(c)}" for c in classes)
            add("CSS", css_sel, PRIORITY["class"], class_contains_xpath(name, classes))

    # 8. Structural fallback (always available, always unique by construction)
    struct_xpath = structural_xpath(tag)
    struct_css = structural_css(tag)
    add("XPath", struct_xpath, PRIORITY["structural"], struct_xpath)
    add("CSS", struct_css, PRIORITY["structural"], struct_xpath)

    # De-duplicate identical (strategy, value) pairs, keep first occurrence
    seen = set()
    deduped = []
    for loc in locators:
        key = (loc["strategy"], loc["value"])
        if key not in seen:
            seen.add(key)
            deduped.append(loc)

    deduped.sort(key=lambda l: l["priority"])
    return deduped


def _is_real_element(node):
    """True for actual tag nodes; False for None or BeautifulSoup's root '[document]' node."""
    name = getattr(node, "name", None)
    return bool(name) and name != "[document]"


def structural_xpath(tag):
    parts = []
    node = tag
    while _is_real_element(node):
        parent = node.parent
        if not _is_real_element(parent):
            parts.append(node.name)
            break
        siblings = parent.find_all(node.name, recursive=False)
        if len(siblings) > 1:
            index = siblings.index(node) + 1
            parts.append(f"{node.name}[{index}]")
        else:
            parts.append(node.name)
        node = parent
    parts.reverse()
    return "/" + "/".join(parts)


def structural_css(tag):
    parts = []
    node = tag
    while _is_real_element(node):
        parent = node.parent
        if not _is_real_element(parent):
            parts.append(node.name)
            break
        siblings = parent.find_all(node.name, recursive=False)
        if len(siblings) > 1:
            index = siblings.index(node) + 1
            parts.append(f"{node.name}:nth-of-type({index})")
        else:
            parts.append(node.name)
        node = parent
    parts.reverse()
    return " > ".join(parts)


# --------------------------------------------------------------------------
# Validation (uniqueness check against the real DOM)
# --------------------------------------------------------------------------

def validate_locators(lxml_tree, elements_with_locators):
    for _, locators in elements_with_locators:
        for loc in locators:
            try:
                matches = lxml_tree.xpath(loc["xpath_check"])
                loc["match_count"] = len(matches)
                loc["valid"] = True
            except etree.XPathEvalError:
                loc["match_count"] = 0
                loc["valid"] = False


# --------------------------------------------------------------------------
# Report generation
# --------------------------------------------------------------------------

def status_badge(loc):
    if not loc["valid"]:
        return "❌ invalid expression"
    if loc["match_count"] == 1:
        return "✅ unique match"
    if loc["match_count"] == 0:
        return "⚠️ 0 matches"
    return f'⚠️ {loc["match_count"]} matches'


def write_report(source, elements_with_locators, output_path, rendered):
    lines = []
    lines.append(f"# Locator Report")
    lines.append("")
    lines.append(f"- **Source:** `{source}`")
    lines.append(f"- **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append(f"- **JS rendering:** {'yes (Playwright)' if rendered else 'no (static HTML only)'}")
    lines.append(f"- **Testable elements found:** {len(elements_with_locators)}")
    lines.append("")
    lines.append("## How to use these locators")
    lines.append("")
    lines.append("| Strategy | Browser DevTools | Selenium | Playwright |")
    lines.append("|---|---|---|---|")
    lines.append('| ID | `document.getElementById("...")` | `By.ID` | `page.locator("#...")` |')
    lines.append('| Name | `document.getElementsByName("...")` | `By.NAME` | `page.locator(\'[name="..."]\')` |')
    lines.append('| CSS | `document.querySelector("...")` | `By.CSS_SELECTOR` | `page.locator("...")` |')
    lines.append('| XPath | `$x("...")` (Console) | `By.XPATH` | `page.locator("xpath=...")` |')
    lines.append('| Link Text | — | `By.LINK_TEXT` | `page.get_by_text("...", exact=True)` |')
    lines.append("")
    lines.append("✅ = confirmed to match exactly one element in the fetched DOM · "
                  "⚠️ = matches 0 or several elements, double-check before use · "
                  "Locators are listed most-recommended first.")
    lines.append("")
    lines.append("## Elements")
    lines.append("")

    for i, (tag, locators) in enumerate(elements_with_locators, start=1):
        label = short_label(tag)
        lines.append(f"### {i}. `<{tag.name}>` — {label}")
        lines.append("")
        lines.append("| Priority | Strategy | Locator | Result |")
        lines.append("|---|---|---|---|")
        for loc in locators:
            priority_text = PRIORITY_LABEL.get(loc["priority"], str(loc["priority"]))
            value_escaped = loc["value"].replace("|", "\\|")
            lines.append(
                f'| {priority_text} | {loc["strategy"]} | `{value_escaped}` | {status_badge(loc)} |'
            )
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def default_output_name(source):
    if re.match(r"^https?://", source, re.I):
        host = urlparse(source).netloc.replace(":", "_")
    else:
        host = os.path.splitext(os.path.basename(source))[0]
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"locators_{host}_{ts}.md"


def main():
    parser = argparse.ArgumentParser(description="Generate test-automation locators for a web page.")
    parser.add_argument("source", help="URL (http/https) or path to a local HTML file")
    parser.add_argument("-o", "--output", default=None, help="Output Markdown file path")
    parser.add_argument("--render", action="store_true",
                         help="Render the page with Playwright first (needed for JS-heavy / SPA sites)")
    parser.add_argument("--max-elements", type=int, default=None,
                         help="Limit the number of elements processed (useful for very large pages)")
    args = parser.parse_args()

    print(f"Fetching: {args.source}{' (rendering JS)' if args.render else ''}")
    try:
        html_content = fetch_html(args.source, render=args.render)
    except Exception as e:
        print(f"[error] Failed to fetch source: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(html_content, "lxml")
    lxml_tree = lxml_html.fromstring(html_content)

    candidates = [tag for tag in soup.find_all(True) if is_testable(tag)]
    if args.max_elements:
        candidates = candidates[: args.max_elements]

    print(f"Found {len(candidates)} testable elements. Generating locators...")

    elements_with_locators = []
    for tag in candidates:
        locators = build_locators(tag)
        elements_with_locators.append((tag, locators))

    validate_locators(lxml_tree, elements_with_locators)

    output_path = args.output or default_output_name(args.source)
    write_report(args.source, elements_with_locators, output_path, rendered=args.render)

    print(f"Done. Report written to: {output_path}")


if __name__ == "__main__":
    main()