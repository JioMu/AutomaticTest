from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.depv")
        print(page.title())
        browser.close()
