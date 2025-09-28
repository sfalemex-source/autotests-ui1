from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    page.get_by_role("textbox",name="Email").click()
    page.get_by_role("textbox", name="Email").fill("user.name@gmail.com")
    page.get_by_role("textbox",name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_test_id("login-page-login-button").click()
    wrong_alert=page.locator('text=Wrong email or password')
    expect(wrong_alert).to_be_visible()
    expect(wrong_alert).to_have_text("Wrong email or password")
    page.wait_for_timeout(5000)



