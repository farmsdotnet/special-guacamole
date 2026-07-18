# Locator Report

- **Source:** `https://example.com`
- **Generated:** 2026-07-18 19:38:45 UTC
- **JS rendering:** no (static HTML only)
- **Testable elements found:** 1

## How to use these locators

| Strategy | Browser DevTools | Selenium | Playwright |
|---|---|---|---|
| ID | `document.getElementById("...")` | `By.ID` | `page.locator("#...")` |
| Name | `document.getElementsByName("...")` | `By.NAME` | `page.locator('[name="..."]')` |
| CSS | `document.querySelector("...")` | `By.CSS_SELECTOR` | `page.locator("...")` |
| XPath | `$x("...")` (Console) | `By.XPATH` | `page.locator("xpath=...")` |
| Link Text | — | `By.LINK_TEXT` | `page.get_by_text("...", exact=True)` |

✅ = confirmed to match exactly one element in the fetched DOM · ⚠️ = matches 0 or several elements, double-check before use · Locators are listed most-recommended first.

## Elements

### 1. `<a>` — Learn more

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learn more` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learn more"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div/p[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div > p:nth-of-type(2) > a` | ✅ unique match |
