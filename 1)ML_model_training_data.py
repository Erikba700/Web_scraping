import pickle
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
This code is unlikely to work due to the following reasons:

1. The CSS selector used to close the modal (`#modals > div > div > div.d-modal__close-button`) is subject to change. 
This may cause the WebDriver to fail to locate and click the close button, breaking the script.

2. The class name `"_item_1ibek_64"` used to find images in the `each_pic_div` part is also likely dynamically 
generated or could change after site updates. If this happens, the script will fail to retrieve images for the items. 
"""


def load_cache() -> dict:
    """
    Loads cached data from a file.

    Returns:
        dict: A dictionary of cached data.
        If no cache is found, an empty dictionary is returned.
    """
    try:
        with open("lamoda_cache_women.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {"data": {}}


def save_cache(this_data: dict) -> None:
    """
    Saves data to a cache file.

    Args:
        this_data (dict): The data to be cached.
    """
    with open("lamoda_cache_women.pkl", "wb") as file:
        pickle.dump(this_data, file)


def parse_links_per_page(page_number: int, page_url: str) -> list[dict[str, str]]:
    """
    Parses all product links on a given page.

    Args:
        page_number (int): The number of the page being parsed.
        page_url (str): The URL of the page to parse.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing item numbers and links.
    """
    response = requests.get(page_url, headers=headers)
    global data
    try:
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "lxml")
        all_items_div = soup.find("div", class_="grid__catalog")
        all_items = all_items_div.find_all(
            "a", class_="x-product-card__link x-product-card__hit-area"
        )
        page_items_dict = []
        for idx, item in enumerate(all_items):
            item_dict = {}
            item_link = f"https://www.lamoda.ru/{item['href']}"
            item_number = f"{page_number}-{idx}"
            item_dict["item_number"] = item_number
            item_dict["item_link"] = item_link
            page_items_dict.append(item_dict)
        return page_items_dict
    except Exception as e:
        print(f"Error occurred during {page_number} page parsing")
        print(e)


def chached_each_pagination(page_number: int) -> None:
    """
    Caches the parsed links for a specific page.

    Args:
        page_number (int): The number of the page to be cached.
    """
    this_page_link = paginated_link.format(page_number)
    print(f"In page {page_number} cached...", flush=True)

    global data, cached_data
    if not cached_data.get(page_number):
        page_items_dict = parse_links_per_page(page_number, this_page_link)

        print(f"Caching finished for page {page_number}", flush=True)

        cached_data["data"][page_number] = page_items_dict
        cached_data[page_number] = True
        save_cache(cached_data)
    else:
        data = cached_data["data"]
        print(f'Page "{page_number}" was cached', flush=True)


def threading_pages_links():
    """
    Manages threading to parse and cache multiple pages concurrently.
    """
    with ThreadPoolExecutor() as executor:
        executor.map(
            lambda page: chached_each_pagination(page),
            [page for page in range(1, page_limit)],
        )


def parse_each_item(page_number: int, item: dict) -> None:
    """
    Parses each item's details and image links.

    Args:
        page_number (int): The page number the item belongs to.
        item (dict): A dictionary containing the item link and item number.
    """
    item_link = item["item_link"]
    item_number = item["item_number"]
    print(f"Processing item {item_number}) {item_link}...")
    global data

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(item_link)
        print("a")
        # Wait up to 10 seconds before throwing a TimeoutException
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#modals > div > div > div.d-modal__close-button")
            )
        )
        element.click()
        driver.execute_script("document.body.style.zoom = '50%';")

        soup = BeautifulSoup(driver.page_source, "lxml")
        each_pic_div = soup.find_all("div", class_="_item_1ibek_64")
        photos_links = []
        for idx, each_pic in enumerate(each_pic_div):
            image_link = each_pic.find("img").get("src")
            photos_links.append(f"{idx}) {image_link}")

        item["pics_links"] = photos_links
        print(f"{len(photos_links)}) photos are saved for link {item_link}")
    except Exception as e:
        print(f"An error occurred: {e} in {item_link}!!!!!!!!!!!")
    finally:
        driver.quit()


def chached_items_of_page(page_number: int) -> None:
    """
    Caches details of all items on a specific page.

    Args:
        page_number (int): The number of the page being processed.
    """
    print(f"------- Parsing items on page {page_number} -------", flush=True)

    global data, cached_data
    if not cached_data.get(f"page_{page_number}_items_chached"):
        with ThreadPoolExecutor() as executor:
            executor.map(
                lambda args: parse_each_item(page_number, args),
                data[page_number][f"page-{page_number}"],
            )
        cached_data["data"] = data
        cached_data[f"page_{page_number}_items_chached"] = True
        save_cache(cached_data)
        print(f"page_{page_number}_items_chached is successfully saved")
        time.sleep(1)
    else:
        print(f'Items of page "{page_number}" were cached', flush=True)


def threading_items():
    """
    Manages threading to parse and cache items across multiple pages.
    """
    for page in range(1, page_limit):
        chached_items_of_page(page)


if __name__ == "__main__":
    # ______________Utility variables____________________
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,hy;q=0.6",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    paginated_link = (
        "https://www.lamoda.ru/c/17/shoes-men/?sitelink=topmenuW&l=4&page={}"
    )
    page_limit = 166
    # ____________Business_Logic______________
    start = time.time()
    data = {"data": {}}
    cached_data = load_cache()

    try:
        threading_pages_links()
        time.sleep(1)

        threading_items()

    except Exception as e:
        print(f"Error occurred in main {e}")
    finally:
        end = time.time()
        print(f"{end - start} secs")
