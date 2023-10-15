from playwright.sync_api import sync_playwright, Playwright
import pytest

@pytest.fixture(autouse=True)
def set_up():
    with sync_playwright() as playwrite:
        browser = playwrite.chromium.launch(headless=False)
        yield browser

        browser.close()