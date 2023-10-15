from playwright.sync_api import sync_playwright, Playwright
import pytest
import os
import time

class TestUltimatix:
    def test_a1(self,set_up):
        self.ultimatix = set_up.new_page()
        self.ultimatix.goto('https://www.ultimatix.net/')
        self.ultimatix.screenshot(path="screenshot1.png")

    def test_a2(self,set_up):
        self.tcs = set_up.new_page()
        self.tcs.goto('https://www.tcs.com/')
        self.tcs.wait_for_timeout(3000)
        self.tcs.click('text=Accept');
        self.tcs.wait_for_timeout(3000)
        self.tcs.hover("//a[text()='Who we are']")
        self.tcs.wait_for_timeout(3000)
        self.tcs.locator('d-flex.justify-content-between.align-items-center.col-3.l2_link.non-overview_link.py-3.px-0.position-relative.tcs-section-click').click()
        self.tcs.wait_for_timeout(3000)
        self.tcs.screenshot(path="screenshot2.png")

