import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
}

# Проверяем ID, который вы видели в DevTools
for pid in [1, 2, 73, 96, 500]:
    url = f"https://scrapingsandbox.com/product/{pid}"
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")

    title = soup.find("h3", class_="product-name")
    price = soup.find("span", class_="price")

    if title and price:
        print(f"ID {pid}: OK — {title.text.strip()} / {price.text.strip()}")
    else:
        print(f"ID {pid}: НЕ НАЙДЕНО (статус {response.status_code}, длина HTML {len(response.text)})")