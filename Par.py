from bs4 import BeautifulSoup

import requests

from Config import MAX_WORKERS

def parse_product(productId):
    url = requests.get(f"https://scrapingsandbox.com/product/{productId}")
    
    soup = BeautifulSoup(url.text, 'lxml')

    titleTag = soup.find("h1", class_="text-2xl")
    priceTag = soup.find("span", class_="text-3xl")

    if not titleTag or not priceTag:
        return None

    name = titleTag.text.strip()
    priceText = priceTag.text.replace("$", "").strip()
    price = float(priceText)

    return{"id": productId, "name": name, "price": price}

def parse_all(product_ids, max_workers):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    all_products = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(parse_product, pid): pid for pid in product_ids}
        for future in as_completed(futures):
            result = future.result()
            if result:
                all_products.append(result)
    return all_products