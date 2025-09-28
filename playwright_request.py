from playwright.sync_api import sync_playwright, Request, Response

def log_request(request:Request):
    print(f'request: {request.url}')

def log_response(response: Response):
    print(f"response: {response.url} {response.status}")



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.on("request",log_request)
    page.on("response",log_response)
    page.remove_listener("request",log_request)
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.wait_for_timeout(5000)

