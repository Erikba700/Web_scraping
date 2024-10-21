import asyncio
from pyppeteer import launch, chromium_downloader
from concurrent.futures import ThreadPoolExecutor


async def main():
    browser = await launch(executablePath=r"C:\Users\erikb\AppData\Local\ms-playwright\chromium-1041\chrome-win\chrome.exe")
    page = await browser.newPage()
    await page.goto('https://karucapatoxic.am/')
    element = await page.querySelector('.MuiTypography-root.MuiTypography-body2.css-60hl1')
    text = await page.evaluate('(element) => element.textContent', element)

    print(element)
    await browser.close()

asyncio.run(main())
