# Locator Finder

A lightweight command-line tool that scans a web page and generates
ready-to-use test-automation locators (ID, CSS selector, XPath, Name,
Link Text, data-testid, aria-label, class, and a structural fallback)
for every interactive element — then writes them to a Markdown report.

Every locator is validated against the page's real DOM before it's
reported, so you know upfront whether it uniquely matches one element
(✅) or is ambiguous (⚠️), rather than finding out during test runs.

## Install

```bash
pip install requests beautifulsoup4 lxml
```

Optional, only needed if you pass `--render` (for React/Vue/Angular
pages whose content is injected by JavaScript after load):

```bash
pip install playwright
playwright install chromium
```

## Usage

```bash
# Basic — writes locators_<host>_<timestamp>.md in the current folder
python locator_finder.py https://example.com

# Choose the output file
python locator_finder.py https://example.com -o example_locators.md

# JS-heavy single-page apps: render with a real browser first
python locator_finder.py https://example.com --render

# Also works on an HTML file you already have saved locally
python locator_finder.py ./saved_page.html

# Cap the number of elements processed on very large pages
python locator_finder.py https://example.com --max-elements 100
```

## What counts as a "testable element"

Links, buttons, inputs, selects, textareas, forms, labels, options,
`<summary>`, and any element carrying a `role`, `onclick`, or
`data-testid`/`data-test`/`data-cy`/`data-qa` attribute.

## How the strategies map to your framework

| Strategy | Browser DevTools | Selenium | Playwright |
|---|---|---|---|
| ID | `document.getElementById("...")` | `By.ID` | `page.locator("#...")` |
| Name | `document.getElementsByName("...")` | `By.NAME` | `page.locator('[name="..."]')` |
| CSS | `document.querySelector("...")` | `By.CSS_SELECTOR` | `page.locator("...")` |
| XPath | `$x("...")` in Console | `By.XPATH` | `page.locator("xpath=...")` |
| Link Text | — | `By.LINK_TEXT` | `page.get_by_text("...", exact=True)` |

Locators are listed most-recommended first: a stable `data-testid` beats
`id`, which beats `name`/`aria-label`, which beats visible text, which
beats a class-based selector, which beats a structural/positional
fallback (the most brittle option — it breaks if the page layout
changes).

## Limitations

- Without `--render`, the tool only sees the HTML returned by the
  initial server response — content injected later by JavaScript won't
  appear. Use `--render` for SPAs.
- Locators are validated for uniqueness against the fetched DOM, not
  against a live browser session, so things like elements hidden by
  CSS or added after further user interaction aren't accounted for.
- Auto-generated / hashed CSS classes (e.g. CSS-in-JS output) are
  filtered out of the class-based suggestions since they tend to change
  on every build.
