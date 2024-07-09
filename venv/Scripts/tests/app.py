from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://playwright.dev/python')
    page.get_by_role('link', name='Docs').click()
    actual_url = page.url
    print('Docs', actual_url)
    browser.close