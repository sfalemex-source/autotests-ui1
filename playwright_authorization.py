from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # email_input=page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    # email_input.fill("user.name@gmail.com")

    #page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("12345@yandex.ru")
    page.wait_for_timeout(5000)
