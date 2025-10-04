from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email_input=page.get_by_test_id("registration-form-email-input").locator('input')
        email_input.fill('testemail')
        username_input=page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('testusername')
        password_input=page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('testpassword')
        reg_button=page.get_by_test_id('registration-page-registration-button')
        reg_button.click()
        context.storage_state(path='test_storage_state.json')

    with sync_playwright() as p:
         browser=p.chromium.launch(headless=False)
         context=browser.new_context(storage_state='test_storage_state.json')
         page=context.new_page()
         page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
         page.wait_for_timeout(5000)