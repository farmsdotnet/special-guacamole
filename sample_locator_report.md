# Locator Report

- **Source:** `sample_test_page.html`
- **Generated:** 2026-07-18 15:19:19 UTC
- **JS rendering:** no (static HTML only)
- **Testable elements found:** 15

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

### 1. `<a>` — Acme Corp

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Acme Corp` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Acme Corp"]` | ✅ unique match |
| Fallback (class) | CSS | `a.logo` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/header/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > header > a` | ✅ unique match |

### 2. `<a>` — Pricing

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Pricing` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Pricing"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/header/nav/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > header > nav > a:nth-of-type(1)` | ✅ unique match |

### 3. `<a>` — About

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `About` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="About"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/header/nav/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > header > nav > a:nth-of-type(2)` | ✅ unique match |

### 4. `<form>` — id="login-form"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `login-form` | ✅ unique match |
| Recommended (id) | CSS | `#login-form` | ✅ unique match |
| Recommended (id) | XPath | `//form[@id="login-form"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/form` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form` | ✅ unique match |

### 5. `<label>` — Email

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/main/form/label[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > label:nth-of-type(1)` | ✅ unique match |

### 6. `<input>` — placeholder="you@example.com"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (test id) | CSS | `[data-testid="email-input"]` | ✅ unique match |
| Recommended (test id) | XPath | `//input[@data-testid="email-input"]` | ✅ unique match |
| Recommended (id) | ID | `email` | ✅ unique match |
| Recommended (id) | CSS | `#email` | ✅ unique match |
| Recommended (id) | XPath | `//input[@id="email"]` | ✅ unique match |
| Good (name) | Name | `email` | ✅ unique match |
| Good (name) | CSS | `input[name="email"]` | ✅ unique match |
| Good (name) | XPath | `//input[@name="email"]` | ✅ unique match |
| OK (placeholder) | CSS | `input[placeholder="you@example.com"]` | ✅ unique match |
| OK (placeholder) | XPath | `//input[@placeholder="you@example.com"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/form/input[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > input:nth-of-type(1)` | ✅ unique match |

### 7. `<label>` — Password

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/main/form/label[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > label:nth-of-type(2)` | ✅ unique match |

### 8. `<input>` — placeholder="Password"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (test id) | CSS | `[data-testid="password-input"]` | ✅ unique match |
| Recommended (test id) | XPath | `//input[@data-testid="password-input"]` | ✅ unique match |
| Recommended (id) | ID | `password` | ✅ unique match |
| Recommended (id) | CSS | `#password` | ✅ unique match |
| Recommended (id) | XPath | `//input[@id="password"]` | ✅ unique match |
| Good (name) | Name | `password` | ✅ unique match |
| Good (name) | CSS | `input[name="password"]` | ✅ unique match |
| Good (name) | XPath | `//input[@name="password"]` | ✅ unique match |
| OK (placeholder) | CSS | `input[placeholder="Password"]` | ✅ unique match |
| OK (placeholder) | XPath | `//input[@placeholder="Password"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/form/input[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > input:nth-of-type(2)` | ✅ unique match |

### 9. `<button>` — Log In

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `submit-button` | ✅ unique match |
| Recommended (id) | CSS | `#submit-button` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="submit-button"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Log In"]` | ✅ unique match |
| Fallback (class) | CSS | `button.btn.btn-primary` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/form/button[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > button:nth-of-type(1)` | ✅ unique match |

### 10. `<button>` — Forgot password?

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Forgot password"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Forgot password"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Forgot password?"]` | ✅ unique match |
| Fallback (class) | CSS | `button.btn.btn-secondary` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/form/button[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > form > button:nth-of-type(2)` | ✅ unique match |

### 11. `<button>` — Continue with Google

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (test id) | CSS | `[data-testid="google-login"]` | ✅ unique match |
| Recommended (test id) | XPath | `//button[@data-testid="google-login"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Continue with Google"]` | ✅ unique match |
| Fallback (class) | CSS | `button.btn.btn-google` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/main/div/button[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > div > button:nth-of-type(1)` | ✅ unique match |

### 12. `<button>` — Continue with Apple

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (test id) | CSS | `[data-testid="apple-login"]` | ✅ unique match |
| Recommended (test id) | XPath | `//button[@data-testid="apple-login"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Continue with Apple"]` | ✅ unique match |
| Fallback (class) | CSS | `button.btn.btn-google` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/main/div/button[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > div > button:nth-of-type(2)` | ✅ unique match |

### 13. `<select>` — id="language-select"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `language-select` | ✅ unique match |
| Recommended (id) | CSS | `#language-select` | ✅ unique match |
| Recommended (id) | XPath | `//select[@id="language-select"]` | ✅ unique match |
| Good (name) | Name | `language` | ✅ unique match |
| Good (name) | CSS | `select[name="language"]` | ✅ unique match |
| Good (name) | XPath | `//select[@name="language"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/main/select` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > select` | ✅ unique match |

### 14. `<option>` — English

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/main/select/option[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > select > option:nth-of-type(1)` | ✅ unique match |

### 15. `<option>` — French

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/main/select/option[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > main > select > option:nth-of-type(2)` | ✅ unique match |
