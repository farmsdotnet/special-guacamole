# Locator Report

- **Source:** `https://www.dynamicyield.com`
- **Generated:** 2026-07-18 19:41:51 UTC
- **JS rendering:** yes (Playwright)
- **Testable elements found:** 220

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

### 1. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.main-logo-container` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(1) > a` | ✅ unique match |

### 2. `<a>` — Product

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Product` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Product"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 3. `<a>` — Solutions

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Solutions` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Solutions"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 4. `<a>` — Why Dynamic Yield

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Why Dynamic Yield` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Why Dynamic Yield"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 5. `<a>` — Company

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Company` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Company"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 6. `<a>` — Learning Center

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learning Center` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learning Center"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 7. `<a>` — Connect with us

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Connect with us` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Connect with us"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/nav/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > nav > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 8. `<a>` — Product

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Product` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Product"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.label` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 9. `<a>` — Get an overview of Dynamic Yield’s product and see why we’re

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Get an overview of Dynamic Yield’s product and see why we’re known as the Experience OS. Learn more →` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Get an overview of Dynamic Yield’s product and see why we’re known as the Experience OS. Learn more →"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[1]/div/ul/li/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(1) > div > ul > li > a` | ✅ unique match |

### 10. `<a>` — Segmentation Identify, build, and analyze audiences

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Segmentation Identify, build, and analyze audiences` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Segmentation Identify, build, and analyze audiences"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 11. `<a>` — Targeting Serve each customer with unique offers

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Targeting Serve each customer with unique offers` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Targeting Serve each customer with unique offers"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 12. `<a>` — Recommendations Algorithmically predict customers’ interests

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Recommendations Algorithmically predict customers’ interests` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Recommendations Algorithmically predict customers’ interests"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 13. `<a>` — Journey Orchestration Reach customers at critical moments

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Journey Orchestration Reach customers at critical moments` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Journey Orchestration Reach customers at critical moments"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 14. `<a>` — Optimization Experiment on any digital property

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Optimization Experiment on any digital property` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Optimization Experiment on any digital property"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 15. `<a>` — Search Help customers find what they want

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Search Help customers find what they want` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Search Help customers find what they want"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 16. `<a>` — Element A groundbreaking new dimension of hyper-personalizat

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Element A groundbreaking new dimension of hyper-personalization` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Element A groundbreaking new dimension of hyper-personalization"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[3]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 17. `<a>` — AI & Automation Increase automation, lower operational costs

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `AI & Automation Increase automation, lower operational costs, and drive more revenue with a holistic AI personalization system` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="AI & Automation Increase automation, lower operational costs, and drive more revenue with a holistic AI personalization system"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[3]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 18. `<a>` — Experience APIs Give developers the tools they need to build

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Experience APIs Give developers the tools they need to build the best customer experiences` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Experience APIs Give developers the tools they need to build the best customer experiences"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[3]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 19. `<a>` — Enterprise solutions Scale with security, privacy, and compl

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Enterprise solutions Scale with security, privacy, and compliance, made for the enterprise` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Enterprise solutions Scale with security, privacy, and compliance, made for the enterprise"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/ul/li[3]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 20. `<a>` — Meet Shopping Muse: Conversational commerce meets cutting-ed

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Meet Shopping Muse: Conversational commerce meets cutting-edge personalization. Learn more →` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Meet Shopping Muse: Conversational commerce meets cutting-edge personalization. Learn more →"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.banner` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[1]/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > div > a` | ✅ unique match |

### 21. `<a>` — Solutions

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Solutions` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Solutions"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.label` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 22. `<a>` — eCommerce

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `eCommerce` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="eCommerce"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 23. `<a>` — Financial Services

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Financial Services` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Financial Services"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 24. `<a>` — Restaurants

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Restaurants` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Restaurants"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 25. `<a>` — Grocery

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Grocery` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Grocery"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 26. `<a>` — B2B eCommerce

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `B2B eCommerce` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="B2B eCommerce"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 27. `<a>` — Travel

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Travel` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Travel"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 28. `<a>` — iGaming

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `iGaming` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="iGaming"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 29. `<a>` — Media

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Media` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Media"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/div/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > div > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 30. `<a>` — Web Create customer-centric web experiences

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Web Create customer-centric web experiences` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Web Create customer-centric web experiences"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 31. `<a>` — Email Personalize emails with a no-code builder

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Email Personalize emails with a no-code builder` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Email Personalize emails with a no-code builder"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 32. `<a>` — Apps Optimize mobile app experiences

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Apps Optimize mobile app experiences` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Apps Optimize mobile app experiences"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 33. `<a>` — Ads Improve customer acquisition results

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Ads Improve customer acquisition results` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Ads Improve customer acquisition results"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(2) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 34. `<a>` — Why Dynamic Yield

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Why Dynamic Yield` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Why Dynamic Yield"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.label` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 35. `<a>` — Select customers

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Select customers` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Select customers"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[1]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 36. `<a>` — Case studies

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Case studies` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Case studies"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[1]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 37. `<a>` — Customer success services

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Customer success services` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Customer success services"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[1]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 38. `<a>` — Enterprise-grade solutions

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Enterprise-grade solutions` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Enterprise-grade solutions"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 39. `<a>` — AI Technology

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `AI Technology` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="AI Technology"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 40. `<a>` — GDPR and data privacy

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `GDPR and data privacy` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="GDPR and data privacy"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 41. `<a>` — Security

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Security` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Security"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 42. `<a>` — Compliance

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Compliance` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Compliance"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(2) > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 43. `<a>` — Partner library

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Partner library` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Partner library"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[3]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(3) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 44. `<a>` — Partnership program

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Partnership program` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Partnership program"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[3]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(3) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 45. `<a>` — Tech Partners and Integrations

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Tech Partners and Integrations` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Tech Partners and Integrations"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[3]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(3) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 46. `<a>` — Knowledge Base

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Knowledge Base` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Knowledge Base"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[4]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(4) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 47. `<a>` — Academy & Certification

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Academy & Certification` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Academy & Certification"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[4]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(4) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 48. `<a>` — Community

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Community` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Community"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[4]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(4) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 49. `<a>` — API documentation

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `API documentation` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="API documentation"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/ul/li[4]/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > ul > li:nth-of-type(4) > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 50. `<a>` — The Personalization Awards Celebrating customers and partner

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `The Personalization Awards Celebrating customers and partners setting the gold-standard for personalization Learn more →` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="The Personalization Awards Celebrating customers and partners setting the gold-standard for personalization Learn more →"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.banner` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[3]/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > div > a` | ✅ unique match |

### 51. `<a>` — Company

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Company` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Company"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.label` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 52. `<a>` — About us

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `About us` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="About us"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 53. `<a>` — Blog

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Blog` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Blog"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 54. `<a>` — DY Labs

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `DY Labs` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="DY Labs"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 55. `<a>` — Careers

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Careers` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Careers"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 56. `<a>` — Events

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Events` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Events"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 57. `<a>` — Press

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Press` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Press"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 58. `<a>` — Awards

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Awards` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Awards"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 59. `<a>` — Contact us

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Contact us` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Contact us"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 60. `<a>` — Request a demo

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Request a demo` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Request a demo"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[4]/div/ul/li[9]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > div > ul > li:nth-of-type(9) > a` | ✅ unique match |

### 61. `<a>` — Learning Center

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learning Center` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learning Center"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.label` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 62. `<a>` — Take your knowledge to exponential levels

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Take your knowledge to exponential levels` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Take your knowledge to exponential levels"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 63. `<a>` — XP 2 Hub Take your knowledge to exponential levels

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `XP 2 Hub Take your knowledge to exponential levels` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="XP 2 Hub Take your knowledge to exponential levels"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 64. `<a>` — Learning Paths Curated courses on key skill areas

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learning Paths Curated courses on key skill areas` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learning Paths Curated courses on key skill areas"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 65. `<a>` — Talks Engaging discussions taking place in CX

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Talks Engaging discussions taking place in CX` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Talks Engaging discussions taking place in CX"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 66. `<a>` — Articles An expansive collection of in-depth playbooks

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Articles An expansive collection of in-depth playbooks` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Articles An expansive collection of in-depth playbooks"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 67. `<a>` — Encyclopedia A glossary of experience optimization terms

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Encyclopedia A glossary of experience optimization terms` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Encyclopedia A glossary of experience optimization terms"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 68. `<a>` — Inspiration Library Personalization examples from real brand

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Inspiration Library Personalization examples from real brands` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Inspiration Library Personalization examples from real brands"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 69. `<a>` — Personalization Maturity How global businesses prioritize pe

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization Maturity How global businesses prioritize personalization` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization Maturity How global businesses prioritize personalization"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 70. `<a>` — Guides & reports Comprehensive topic-specific materials

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Guides & reports Comprehensive topic-specific materials` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Guides & reports Comprehensive topic-specific materials"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[9]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(9) > a` | ✅ unique match |

### 71. `<a>` — Benchmarks Industry performance metrics and insights

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Benchmarks Industry performance metrics and insights` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Benchmarks Industry performance metrics and insights"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/ul/li[10]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(1) > ul > li:nth-of-type(10) > a` | ✅ unique match |

### 72. `<a>` — Rooted Personalization new Learn a scalable methodology for 

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Rooted Personalization new Learn a scalable methodology for building an audience-based personalization program. Find out more →` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Rooted Personalization new Learn a scalable methodology for building an audience-based personalization program. Find out more →"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[5]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 73. `<a>` — Connect with us

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Connect with us` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Connect with us"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[2]/div/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 74. `<a>` — English

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `English` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="English"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.active` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/div/ul/li/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > div > ul > li > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 75. `<a>` — Español

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Español` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Español"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/div/ul/li/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > div > ul > li > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 76. `<a>` — Deutsch

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Deutsch` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Deutsch"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/div/ul/li/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > div > ul > li > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 77. `<a>` — Français

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Français` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Français"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/div/ul/li/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > div > ul > li > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 78. `<a>` — 日本語

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `日本語` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="日本語"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/div/ul/li/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > div > ul > li > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 79. `<a>` — Talk to sales

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Talk to sales` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Talk to sales"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.pulse-button.v5.pulsed` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > a:nth-of-type(1)` | ✅ unique match |

### 80. `<a>` — Login

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Login` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Login"]` | ✅ unique match |
| Fallback (class) | CSS | `a.login-btn.dyother.dyMonitor` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > a:nth-of-type(2)` | ✅ unique match |

### 81. `<a>` — Open Nav

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Open Nav` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Open Nav"]` | ✅ unique match |
| Fallback (class) | CSS | `a.nav-trigger` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/header/div/div[3]/a[3]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > header > div > div:nth-of-type(3) > a:nth-of-type(3)` | ✅ unique match |

### 82. `<a>` — Get a Demo

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Get a Demo` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Get a Demo"]` | ✅ unique match |
| Fallback (class) | CSS | `a.header-btn` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[1]/div/div[1]/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(1) > div > div:nth-of-type(1) > div > a` | ✅ unique match |

### 83. `<a>` — Experience OS

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Experience OS` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Experience OS"]` | ✅ unique match |
| Fallback (class) | CSS | `a.ex-os-bold` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[1]/div/div[2]/div/p[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(1) > div > div:nth-of-type(2) > div > p:nth-of-type(2) > a` | ✅ unique match |

### 84. `<button>` — Previous

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Previous"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Previous"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Previous"]` | ✅ unique match |
| Fallback (class) | CSS | `button.slick-prev.slick-arrow.slick-disabled` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/button[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > button:nth-of-type(1)` | ✅ unique match |

### 85. `<a>` — Read his story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read his story` | ⚠️ 4 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read his story"]` | ⚠️ 4 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[1]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(1) > div > div > a` | ✅ unique match |

### 86. `<a>` — Read her story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read her story` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read her story"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[2]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(2) > div > div > a` | ✅ unique match |

### 87. `<a>` — Read her story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read her story` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read her story"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[3]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(3) > div > div > a` | ✅ unique match |

### 88. `<a>` — Read his story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read his story` | ⚠️ 4 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read his story"]` | ⚠️ 4 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[4]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(4) > div > div > a` | ✅ unique match |

### 89. `<a>` — Read his story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read his story` | ⚠️ 4 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read his story"]` | ⚠️ 4 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[5]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(5) > div > div > a` | ✅ unique match |

### 90. `<a>` — Read his story

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read his story` | ⚠️ 4 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read his story"]` | ⚠️ 4 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/div/div/div[6]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > div > div > div:nth-of-type(6) > div > div > a` | ✅ unique match |

### 91. `<button>` — Next

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Next"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Next"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Next"]` | ✅ unique match |
| Fallback (class) | CSS | `button.slick-next.slick-arrow` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[2]/div/div/div/div/button[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(2) > div > div > div > div > button:nth-of-type(2)` | ✅ unique match |

### 92. `<a>` — Read the Gartner® report →

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read the Gartner® report →` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read the Gartner® report →"]` | ✅ unique match |
| Fallback (class) | CSS | `a.gbc-cta` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(3) > div > div > div > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > a` | ✅ unique match |

### 93. `<a>` — Read the Forrester report →

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Read the Forrester report →` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Read the Forrester report →"]` | ✅ unique match |
| Fallback (class) | CSS | `a.gbc-cta` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[3]/div/div/div/div/div/div/div[3]/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(3) > div > div > div > div > div > div > div:nth-of-type(3) > div:nth-of-type(2) > a` | ✅ unique match |

### 94. `<a>` — Discover Identify, build, and analyze audiences

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Discover Identify, build, and analyze audiences` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Discover Identify, build, and analyze audiences"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[4]/div[2]/div/div/div[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(4) > div:nth-of-type(2) > div > div > div:nth-of-type(1) > a` | ✅ unique match |

### 95. `<a>` — Target Personalize content and offers to each customer

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Target Personalize content and offers to each customer` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Target Personalize content and offers to each customer"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[4]/div[2]/div/div/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(4) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > a` | ✅ unique match |

### 96. `<a>` — Recommend Algorithmically predict customers’ interests

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Recommend Algorithmically predict customers’ interests` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Recommend Algorithmically predict customers’ interests"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[4]/div[2]/div/div/div[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(4) > div:nth-of-type(2) > div > div > div:nth-of-type(3) > a` | ✅ unique match |

### 97. `<a>` — Engage Reach customers at critical moments

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Engage Reach customers at critical moments` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Engage Reach customers at critical moments"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[4]/div[2]/div/div/div[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(4) > div:nth-of-type(2) > div > div > div:nth-of-type(4) > a` | ✅ unique match |

### 98. `<a>` — Optimize Experiment anywhere on your digital properties

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Optimize Experiment anywhere on your digital properties` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Optimize Experiment anywhere on your digital properties"]` | ⚠️ 0 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[4]/div[2]/div/div/div[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(4) > div:nth-of-type(2) > div > div > div:nth-of-type(5) > a` | ✅ unique match |

### 99. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.testimonial-play-video.video__play__button` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[5]/div/div/div[2]/div/span/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(5) > div > div > div:nth-of-type(2) > div > span > div > div > a` | ✅ unique match |

### 100. `<a>` — See more customer stories

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `See more customer stories` | ⚠️ 3 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="See more customer stories"]` | ⚠️ 3 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[5]/div/div/div[3]/div[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(5) > div > div > div:nth-of-type(3) > div:nth-of-type(1) > a` | ✅ unique match |

### 101. `<a>` — See more customer stories

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `See more customer stories` | ⚠️ 3 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="See more customer stories"]` | ⚠️ 3 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[5]/div/div/div[3]/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(5) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > a` | ✅ unique match |

### 102. `<a>` — See more customer stories

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `See more customer stories` | ⚠️ 3 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="See more customer stories"]` | ⚠️ 3 matches |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[5]/div/div/div[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(5) > div > div > div:nth-of-type(4) > a` | ✅ unique match |

### 103. `<a>` — personalization examples

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `personalization examples` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="personalization examples"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[6]/div[1]/div[1]/div/p/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(6) > div:nth-of-type(1) > div:nth-of-type(1) > div > p > a:nth-of-type(1)` | ✅ unique match |

### 104. `<a>` — experience building templates

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `experience building templates` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="experience building templates"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[6]/div[1]/div[1]/div/p/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(6) > div:nth-of-type(1) > div:nth-of-type(1) > div > p > a:nth-of-type(2)` | ✅ unique match |

### 105. `<a>` — Learn more about our Customer Success services

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learn more about our Customer Success services` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learn more about our Customer Success services"]` | ✅ unique match |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[6]/div[1]/div[1]/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(6) > div:nth-of-type(1) > div:nth-of-type(1) > div > a` | ✅ unique match |

### 106. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(1) > a` | ✅ unique match |

### 107. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(2) > a` | ✅ unique match |

### 108. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(3) > a` | ✅ unique match |

### 109. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(4) > a` | ✅ unique match |

### 110. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(5) > a` | ✅ unique match |

### 111. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(6) > a` | ✅ unique match |

### 112. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(7) > a` | ✅ unique match |

### 113. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/div[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(8) > a` | ✅ unique match |

### 114. `<a>` — Explore all integrations

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Explore all integrations` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Explore all integrations"]` | ✅ unique match |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[1]/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(1) > div > a` | ✅ unique match |

### 115. `<a>` — Explore our partners

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Explore our partners` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Explore our partners"]` | ✅ unique match |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[7]/div[2]/div[2]/div[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(7) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > a` | ✅ unique match |

### 116. `<a>` — Multiply your experience optimization results

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Multiply your experience optimization results` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Multiply your experience optimization results"]` | ✅ unique match |
| Fallback (class) | CSS | `a.link-arrow` | ⚠️ 13 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[1]/div/div/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(1) > div > div > a` | ✅ unique match |

### 117. `<a>` — A/B Testing & Optimization 15 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `A/B Testing & Optimization 15 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="A/B Testing & Optimization 15 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(1)` | ✅ unique match |

### 118. `<a>` — Personalization & Targeting 12 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization & Targeting 12 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization & Targeting 12 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(2)` | ✅ unique match |

### 119. `<a>` — Product Recommendations 7 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Product Recommendations 7 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Product Recommendations 7 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[3]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(3)` | ✅ unique match |

### 120. `<a>` — CRO and Growth Marketing 13 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `CRO and Growth Marketing 13 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="CRO and Growth Marketing 13 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[4]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(4)` | ✅ unique match |

### 121. `<a>` — eCommerce Experience Optimization 9 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `eCommerce Experience Optimization 9 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="eCommerce Experience Optimization 9 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[5]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(5)` | ✅ unique match |

### 122. `<a>` — Advanced Experimentation 9 Lessons Explore now

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Advanced Experimentation 9 Lessons Explore now` | ⚠️ 0 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Advanced Experimentation 9 Lessons Explore now"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `a.hp-lc-item` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[2]/div/a[6]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > a:nth-of-type(6)` | ✅ unique match |

### 123. `<a>` — An introduction to website personalization, with examples

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `An introduction to website personalization, with examples` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="An introduction to website personalization, with examples"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[1]/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > a:nth-of-type(1)` | ✅ unique match |

### 124. `<a>` — Shopping cart abandonment recovery strategies

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Shopping cart abandonment recovery strategies` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Shopping cart abandonment recovery strategies"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[1]/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > a:nth-of-type(2)` | ✅ unique match |

### 125. `<a>` — A/B testing and experimentation: A beginner's guide

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `A/B testing and experimentation: A beginner's guide` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="A/B testing and experimentation: A beginner's guide"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[1]/a[3]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > a:nth-of-type(3)` | ✅ unique match |

### 126. `<a>` — Product recommendation techniques proven to get results

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Product recommendation techniques proven to get results` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Product recommendation techniques proven to get results"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[1]/a[4]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > a:nth-of-type(4)` | ✅ unique match |

### 127. `<a>` — Developing a conversion rate optimization strategy

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Developing a conversion rate optimization strategy` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Developing a conversion rate optimization strategy"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[1]/a[5]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > a:nth-of-type(5)` | ✅ unique match |

### 128. `<a>` — Banking’s Personalization Revolution: Data-Driven Transforma

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Banking’s Personalization Revolution: Data-Driven Transformation` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Banking’s Personalization Revolution: Data-Driven Transformation"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[2]/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(2) > a:nth-of-type(1)` | ✅ unique match |

### 129. `<a>` — The Revenue Gains From Personalization That Financial Instit

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `The Revenue Gains From Personalization That Financial Institutions Can’t Ignore` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="The Revenue Gains From Personalization That Financial Institutions Can’t Ignore"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[2]/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(2) > a:nth-of-type(2)` | ✅ unique match |

### 130. `<a>` — Why A/B Testing and Personalization Are at Their Best Togeth

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Why A/B Testing and Personalization Are at Their Best Together` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Why A/B Testing and Personalization Are at Their Best Together"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[2]/a[3]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(2) > a:nth-of-type(3)` | ✅ unique match |

### 131. `<a>` — A reference manual for picking a personalization vendor

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `A reference manual for picking a personalization vendor` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="A reference manual for picking a personalization vendor"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[3]/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(3) > a:nth-of-type(1)` | ✅ unique match |

### 132. `<a>` — Amazon: The chronicles of a personalization giant

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Amazon: The chronicles of a personalization giant` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Amazon: The chronicles of a personalization giant"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[3]/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(3) > a:nth-of-type(2)` | ✅ unique match |

### 133. `<a>` — Gartner 2026 Magic Quadrant for Personalization Engines

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Gartner 2026 Magic Quadrant for Personalization Engines` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Gartner 2026 Magic Quadrant for Personalization Engines"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[3]/a[3]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(3) > a:nth-of-type(3)` | ✅ unique match |

### 134. `<a>` — The Ultimate Guide to Personalization for Restaurants

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `The Ultimate Guide to Personalization for Restaurants` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="The Ultimate Guide to Personalization for Restaurants"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[3]/a[4]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(3) > a:nth-of-type(4)` | ✅ unique match |

### 135. `<a>` — Frost & Sullivan Visionary Leadership Report

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Frost & Sullivan Visionary Leadership Report` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Frost & Sullivan Visionary Leadership Report"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/div/article/div/div[8]/div[2]/div/div[3]/div/div/div[3]/a[5]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > article > div > div:nth-of-type(8) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(3) > a:nth-of-type(5)` | ✅ unique match |

### 136. `<a>` — Contact Sales

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Contact Sales` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Contact Sales"]` | ✅ unique match |
| Fallback (class) | CSS | `a.btn-teal` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/div/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > div > a:nth-of-type(1)` | ✅ unique match |

### 137. `<a>` — Watch a product demo

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Watch a product demo` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Watch a product demo"]` | ✅ unique match |
| Fallback (class) | CSS | `a.btn-transparent` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/div/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > div > a:nth-of-type(2)` | ✅ unique match |

### 138. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 139. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 140. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 141. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[1]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(1) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 142. `<a>` — Segmentation

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Segmentation` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Segmentation"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[1]/div/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 143. `<a>` — Targeting

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Targeting` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Targeting"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[1]/div/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 144. `<a>` — Recommendations

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Recommendations` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Recommendations"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[1]/div/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 145. `<a>` — Journey Orchestration

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Journey Orchestration` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Journey Orchestration"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[1]/div/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 146. `<a>` — Optimization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Optimization` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Optimization"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[1]/div/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 147. `<a>` — eCommerce

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `eCommerce` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="eCommerce"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 148. `<a>` — Financial Services

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Financial Services` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Financial Services"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 149. `<a>` — Restaurants

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Restaurants` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Restaurants"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 150. `<a>` — Grocery

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Grocery` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Grocery"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 151. `<a>` — B2B eCommerce

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `B2B eCommerce` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="B2B eCommerce"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 152. `<a>` — Travel

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Travel` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Travel"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 153. `<a>` — iGaming

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `iGaming` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="iGaming"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 154. `<a>` — Media

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Media` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Media"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[2]/div/div/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 155. `<a>` — Industry-Leading Services

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Industry-Leading Services` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Industry-Leading Services"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 156. `<a>` — Global Scale

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Global Scale` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Global Scale"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 157. `<a>` — Real Impact

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Real Impact` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Real Impact"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 158. `<a>` — Personalization AI

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization AI` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization AI"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 159. `<a>` — Rich Partner Network

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Rich Partner Network` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Rich Partner Network"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 160. `<a>` — Enterprise-Grade Security

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Enterprise-Grade Security` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Enterprise-Grade Security"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[3]/div/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 161. `<a>` — About Us

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `About Us` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="About Us"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 162. `<a>` — Events

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Events` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Events"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 163. `<a>` — Press

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Press` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Press"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 164. `<a>` — Blog

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Blog` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Blog"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 165. `<a>` — Contact

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Contact` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Contact"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 166. `<a>` — Become a Partner

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Become a Partner` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Become a Partner"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 167. `<a>` — Request Demo

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Request Demo` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Request Demo"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[1]/div/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(1) > div > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 168. `<a>` — We’re hiring!

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `We’re hiring!` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="We’re hiring!"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[4]/div[2]/div/ul/li/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(4) > div:nth-of-type(2) > div > ul > li > a` | ✅ unique match |

### 169. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.lc-footer-logo` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(1) > a` | ✅ unique match |

### 170. `<a>` — Articles

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Articles` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Articles"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 171. `<a>` — Learning Paths

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Learning Paths` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Learning Paths"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 172. `<a>` — Rooted Personalization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Rooted Personalization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Rooted Personalization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 173. `<a>` — Personalization Examples

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization Examples` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization Examples"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 174. `<a>` — Guides

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Guides` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Guides"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 175. `<a>` — Talks

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Talks` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Talks"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 176. `<a>` — Encyclopedia

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Encyclopedia` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Encyclopedia"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 177. `<a>` — Benchmarks

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Benchmarks` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Benchmarks"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[2]/div/div[5]/div[2]/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(2) > div > div:nth-of-type(5) > div:nth-of-type(2) > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 178. `<a>` — Recommended Guides:

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Recommended Guides:` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Recommended Guides:"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 179. `<a>` — Personalization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 180. `<a>` — A/B Testing

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `A/B Testing` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="A/B Testing"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 181. `<a>` — Conversion Rate Optimization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Conversion Rate Optimization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Conversion Rate Optimization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 182. `<a>` — Shopping Cart Abandonment

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Shopping Cart Abandonment` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Shopping Cart Abandonment"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 183. `<a>` — Product Recommendations

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Product Recommendations` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Product Recommendations"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 184. `<a>` — Omnichannel Retailing

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Omnichannel Retailing` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Omnichannel Retailing"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[7]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(7) > a` | ✅ unique match |

### 185. `<a>` — eCommerce Conversion Rate Optimization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `eCommerce Conversion Rate Optimization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="eCommerce Conversion Rate Optimization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[8]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(8) > a` | ✅ unique match |

### 186. `<a>` — Personalization Statistics

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Personalization Statistics` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Personalization Statistics"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[9]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(9) > a` | ✅ unique match |

### 187. `<a>` — Checkout Optimization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Checkout Optimization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Checkout Optimization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[10]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(10) > a` | ✅ unique match |

### 188. `<a>` — eCommerce Personalization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `eCommerce Personalization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="eCommerce Personalization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[11]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(11) > a` | ✅ unique match |

### 189. `<a>` — Omnichannel Personalization

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Omnichannel Personalization` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Omnichannel Personalization"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[12]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(12) > a` | ✅ unique match |

### 190. `<a>` — Shopping Cart Abandonment Rate

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Shopping Cart Abandonment Rate` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Shopping Cart Abandonment Rate"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/ul/li[13]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > ul > li:nth-of-type(13) > a` | ✅ unique match |

### 191. `<a>` — English

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `English` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="English"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `a.active` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/div[2]/ul/li/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > div:nth-of-type(2) > ul > li > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 192. `<a>` — Español

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Español` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Español"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/div[2]/ul/li/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > div:nth-of-type(2) > ul > li > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 193. `<a>` — Deutsch

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Deutsch` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Deutsch"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/div[2]/ul/li/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > div:nth-of-type(2) > ul > li > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 194. `<a>` — Français

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Français` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="Français"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/div[2]/ul/li/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > div:nth-of-type(2) > ul > li > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 195. `<a>` — 日本語

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `日本語` | ⚠️ 2 matches |
| Good (visible text) | XPath | `//a[normalize-space(text())="日本語"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[3]/div/div[2]/ul/li/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(3) > div > div:nth-of-type(2) > ul > li > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 196. `<button>` — Manage cookies

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `ot-sdk-btn` | ✅ unique match |
| Recommended (id) | CSS | `#ot-sdk-btn` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="ot-sdk-btn"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Manage cookies"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `button.ot-sdk-show-settings` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[1]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(1) > div > button` | ✅ unique match |

### 197. `<a>` — Privacy Notice

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Privacy Notice` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Privacy Notice"]` | ✅ unique match |
| Fallback (class) | CSS | `a.animlink` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[1]/div/a[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(1) > div > a:nth-of-type(1)` | ✅ unique match |

### 198. `<a>` — Terms of use

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (visible text) | Link Text | `Terms of use` | ✅ unique match |
| Good (visible text) | XPath | `//a[normalize-space(text())="Terms of use"]` | ✅ unique match |
| Fallback (class) | CSS | `a.animlink` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[1]/div/a[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(1) > div > a:nth-of-type(2)` | ✅ unique match |

### 199. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[1]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(1) > a` | ✅ unique match |

### 200. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[2]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(2) > a` | ✅ unique match |

### 201. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[3]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(3) > a` | ✅ unique match |

### 202. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[4]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(4) > a` | ✅ unique match |

### 203. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[5]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(5) > a` | ✅ unique match |

### 204. `<a>` — <a> (no visible text)

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Fallback (class) | CSS | `a.icon` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[2]/div[2]/footer/div[4]/div/div[2]/span/ul/li[6]/a` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(2) > div:nth-of-type(2) > footer > div:nth-of-type(4) > div > div:nth-of-type(2) > span > ul > li:nth-of-type(6) > a` | ✅ unique match |

### 205. `<div>` — aria-label="Dynamic Yield Product Teaser"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `wistia-uf4hsb47z9-1_popover_container` | ✅ unique match |
| Recommended (id) | CSS | `#wistia-uf4hsb47z9-1_popover_container` | ✅ unique match |
| Recommended (id) | XPath | `//div[@id="wistia-uf4hsb47z9-1_popover_container"]` | ✅ unique match |
| Good (aria-label) | CSS | `div[aria-label="Dynamic Yield Product Teaser"]` | ✅ unique match |
| Good (aria-label) | XPath | `//div[@aria-label="Dynamic Yield Product Teaser"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5)` | ✅ unique match |

### 206. `<button>` — aria-label="Play Video: Dynamic Yield Product Teaser"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Play Video: Dynamic Yield Product Teaser"]` | ⚠️ 2 matches |
| Good (aria-label) | XPath | `//button[@aria-label="Play Video: Dynamic Yield Product Teaser"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `button.w-css-reset.w-vulcan-v2-button` | ⚠️ 6 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(2) > button` | ✅ unique match |

### 207. `<button>` — aria-label="Play Video: Dynamic Yield Product Teaser"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Play Video: Dynamic Yield Product Teaser"]` | ⚠️ 2 matches |
| Good (aria-label) | XPath | `//button[@aria-label="Play Video: Dynamic Yield Product Teaser"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `button.w-big-play-button.w-css-reset-button-important.w-vulcan-v2-button` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(3) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > button` | ✅ unique match |

### 208. `<button>` — Click for sound

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Click for sound"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Click for sound"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Click for sound"]` | ⚠️ 0 matches |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.click-for-sound-btn` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(3) > div:nth-of-type(2) > div > div:nth-of-type(2) > div > button` | ✅ unique match |

### 209. `<button>` — aria-label="Play Video"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Play Video"]` | ⚠️ 2 matches |
| Good (aria-label) | XPath | `//button[@aria-label="Play Video"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `button.w-vulcan-v2-button` | ⚠️ 9 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[5]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(3) > div:nth-of-type(2) > div > div:nth-of-type(5) > div > button` | ✅ unique match |

### 210. `<button>` — aria-label="Play Video"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Play Video"]` | ⚠️ 2 matches |
| Good (aria-label) | XPath | `//button[@aria-label="Play Video"]` | ⚠️ 2 matches |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.w-css-reset.w-css-reset-tree` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(3) > div > div > div > button` | ✅ unique match |

### 211. `<div>` — aria-label="Playbar"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `div[aria-label="Playbar"]` | ✅ unique match |
| Good (aria-label) | XPath | `//div[@aria-label="Playbar"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[4]/div/div/div/div[2]/div` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(4) > div > div > div > div:nth-of-type(2) > div` | ✅ unique match |

### 212. `<button>` — aria-label="Show captions menu"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Show captions menu"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Show captions menu"]` | ✅ unique match |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.w-css-reset.w-css-reset-tree` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[5]/div[1]/div/div[1]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(1) > div > button` | ✅ unique match |

### 213. `<button>` — aria-label="Mute"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Mute"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Mute"]` | ✅ unique match |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.w-css-reset.w-css-reset-tree` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[5]/div[1]/div/div[2]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(2) > div > button` | ✅ unique match |

### 214. `<button>` — aria-label="Show settings menu"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Show settings menu"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Show settings menu"]` | ✅ unique match |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.w-css-reset.w-css-reset-tree` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[5]/div[1]/div/div[3]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(3) > div > button` | ✅ unique match |

### 215. `<button>` — aria-label="Fullscreen"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `button[aria-label="Fullscreen"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Fullscreen"]` | ✅ unique match |
| Fallback (class) | CSS | `button.w-vulcan-v2-button.w-css-reset.w-css-reset-tree` | ⚠️ 5 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[5]/div[1]/div/div[4]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(4) > div > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(4) > div > button` | ✅ unique match |

### 216. `<button>` — aria-label="Close"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `wistia-uf4hsb47z9-1_popover_popover_close_button` | ✅ unique match |
| Recommended (id) | CSS | `#wistia-uf4hsb47z9-1_popover_popover_close_button` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="wistia-uf4hsb47z9-1_popover_popover_close_button"]` | ✅ unique match |
| Good (aria-label) | CSS | `button[aria-label="Close"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Close"]` | ✅ unique match |
| Fallback (class) | CSS | `button.wistia_placebo_close_button` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[5]/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(5) > button` | ✅ unique match |

### 217. `<div>` — aria-label="How we use cookies and your consent"

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Good (aria-label) | CSS | `div[aria-label="How we use cookies and your consent"]` | ✅ unique match |
| Good (aria-label) | XPath | `//div[@aria-label="How we use cookies and your consent"]` | ✅ unique match |
| Fallback (class) | CSS | `div.ot-sdk-container` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[6]/div[2]/div` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(6) > div:nth-of-type(2) > div` | ✅ unique match |

### 218. `<button>` — Manage cookies

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `onetrust-pc-btn-handler` | ✅ unique match |
| Recommended (id) | CSS | `#onetrust-pc-btn-handler` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="onetrust-pc-btn-handler"]` | ✅ unique match |
| Good (aria-label) | CSS | `button[aria-label="Manage cookies, Opens the preference center dialog"]` | ✅ unique match |
| Good (aria-label) | XPath | `//button[@aria-label="Manage cookies, Opens the preference center dialog"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Manage cookies"]` | ⚠️ 2 matches |
| Fallback (structural / brittle) | XPath | `/html/body/div[6]/div[2]/div/div/div[2]/div/button` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(6) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > button` | ✅ unique match |

### 219. `<button>` — Reject all

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `onetrust-reject-all-handler` | ✅ unique match |
| Recommended (id) | CSS | `#onetrust-reject-all-handler` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="onetrust-reject-all-handler"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Reject all"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[6]/div[2]/div/div/div[2]/div/div/button[1]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(6) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > button:nth-of-type(1)` | ✅ unique match |

### 220. `<button>` — Accept cookies

| Priority | Strategy | Locator | Result |
|---|---|---|---|
| Recommended (id) | ID | `onetrust-accept-btn-handler` | ✅ unique match |
| Recommended (id) | CSS | `#onetrust-accept-btn-handler` | ✅ unique match |
| Recommended (id) | XPath | `//button[@id="onetrust-accept-btn-handler"]` | ✅ unique match |
| Good (visible text) | XPath | `//button[normalize-space(text())="Accept cookies"]` | ✅ unique match |
| Fallback (structural / brittle) | XPath | `/html/body/div[6]/div[2]/div/div/div[2]/div/div/button[2]` | ✅ unique match |
| Fallback (structural / brittle) | CSS | `html > body > div:nth-of-type(6) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > button:nth-of-type(2)` | ✅ unique match |
