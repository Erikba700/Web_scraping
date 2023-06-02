from playwright.sync_api import Playwright, sync_playwright, expect
import time

"""
class registration

For my university courses, I have created a script that automatically logs in to the system
and chooses the courses very fast instead of me since a lot of students log in to the
the system at the same time, and it is very crucial to be fast in registering for your
desired coursed.

Author: Erik Badalyan
Date: Jan 2023

"""


def run(playwright: Playwright) -> None:
    while True:
        try:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://im.aua.am/Account/Login")
            page.locator("#UserName").click()
            page.locator("#UserName").fill("erik_badalyan@edu.aua.am")
            page.locator("#UserName").press("Tab")
            page.locator("#Password").fill("Addcry700")
            page.locator("#Password").press("Enter")
            time.sleep(1)
            page.get_by_text("Student").click()
            page.get_by_role("link", name="My Classes").click()
            page.get_by_role("link", name="Register for Classes").click()
            page.get_by_role("row",
                             name="LAW 142 - Introduction to Human Rights B Spring 2023 2023-0"
                                  "1-18 / 2023-05-13 3 15 Week Course Add to My Classes").get_by_role(
                "link", name="Add to My Classes").click()
            time.sleep(2000)
            # ---------------------
            context.close()
            browser.close()
        except Exception:
            print('Not working')


with sync_playwright() as playwright:
    run(playwright)
