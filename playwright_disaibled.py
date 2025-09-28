from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_but=page.get_by_test_id('login-page-login-button')
    expect(login_but).to_be_disabled()