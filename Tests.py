import os
import time

from playwright.sync_api import sync_playwright

outputFolder = "output/"


def test_case_1():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        final_name = outputFolder + "1.png"
        page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path=final_name)
        browser.close()
        assert os.path.exists(final_name)


def test_case_2():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        final_name = outputFolder + "2.png"
        page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path=final_name)
        browser.close()
        assert os.path.exists(final_name)


def test_case_3():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        final_name = outputFolder + "3.png"
        page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)").screenshot(path=final_name)
        browser.close()
        assert os.path.exists(final_name)
