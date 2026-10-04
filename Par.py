from bs4 import BeautifulSoup

import requests, time

from Config import URL, headers

def parse_product(productId, max_retries=3):
    url = f"{URL}{productId}"
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                return None
            

            soup = BeautifulSoup(response.text, 'lxml')
            

            titleTag = soup.find("h1", class_="text-2xl")
            priceTag = soup.find("span", class_="text-3xl")

            if not titleTag or not priceTag:
                return None

            name = titleTag.text.strip()
            priceText = priceTag.text.replace("$", "").strip()
            price = float(priceText)

            return{"id": productId, "name": name, "price": price}
        
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Ошибка на ID {productId}: {e}, не удалось после {max_retries}")
                return None
            time.sleep(1)

def parse_all(product_ids, max_workers = 10):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    all_products = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(parse_product, pid): pid for pid in product_ids}
        for future in as_completed(futures):
            result = future.result()
            if result:
                all_products.append(result)
    return all_products