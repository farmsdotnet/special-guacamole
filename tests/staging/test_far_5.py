from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage


def test_far_5():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        try:
            # Clear out the AI's duplicated browser/page initialisation lines
            login_page = LoginPage(page)
            login_page.login('problem_user', 'secret_sauce')

            # Use page.goto instead of the incorrect page.navigate
            page.goto('https://saucedemo.com')

            print("🚀 Test executed successfully!")
        finally:
            context.close()
            browser.close()
