from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

while True:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto('https://elearning.aua.am/login/index.php')
        page.fill('input#username', 'erik_badalyan')
        page.fill('input#password', 'Addcry700')
        page.click('button[type=submit]')
        page.click('a#action-menu-toggle-0')
        page.click('span#actionmenuaction-3')
        html = page.inner_html('#overview-grade')
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.find_all('td', calss_='cell c1'))


