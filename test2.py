from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    reg_email=page.get_by_test_id('registration-form-email-input').locator('input')
    reg_email.fill("user.name@gmail.com")
    reg_username=page.get_by_test_id('registration-form-username-input').locator('input')
    reg_username.fill("username")
    reg_pass=page.get_by_test_id('registration-form-password-input').locator('input')
    reg_pass.fill("password")
    reg_but=page.get_by_test_id('registration-page-registration-button').click()
    dash_text=page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dash_text).to_have_text("Dashboard")

    page.wait_for_timeout(5000)


