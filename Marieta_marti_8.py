import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/")
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").fill("marti.8.d.shnorhavor")
    page.get_by_label("Phone number, username, or email").press("Tab")
    page.get_by_label("Password").fill("Marieta")
    page.get_by_label("Password").press("Enter")
    time.sleep(5)
    page.get_by_role("link", name="Direct messaging - 0 new notifications link").click()
    time.sleep(3)
    page.get_by_role("button", name="Not Now").click()
    time.sleep(0.5)
    page.get_by_role("button", name="User avatar stepaniiaan").click()
    time.sleep(1)
    page.get_by_role("link", name="stepaniiaan").click()
    time.sleep(4)
    page.get_by_role("link", name="The view💘 Carousel 78 14").click()
    time.sleep(6)
    while True:
        page.get_by_placeholder("Add a comment…").click()
        time.sleep(0.4)
        page.get_by_placeholder("Add a comment…").fill("ես եմ առաջարկել, բայց սրանից հետո էլ առաջարկներս չընդունես, "
                                                       "մարտի 8դ էլ շնորհավոր)")
        page.get_by_placeholder("Add a comment…").press("Enter")
        time.sleep(1.4)



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
