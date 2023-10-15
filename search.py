from playwright.sync_api import sync_playwright, Playwright

with sync_playwright() as playwrite:
    browser = playwrite.chromium.launch(headless=False)
    context = browser.new_page()
    page = context.goto('https://www.google.com')

