# main.py

import time
from Config import FIRSTID, MAXID, MAX_WORKERS, MIN_PRICE, MAX_PRICE
from Par import parse_all


def main():
    start = time.time()

    product_ids = range(FIRSTID, MAXID)
    all_products = parse_all(product_ids, max_workers=MAX_WORKERS)

    elapsed = time.time() - start
    print(f"Всего товаров: {len(all_products)}")
    print(f"Время: {elapsed:.1f} секунд")

    filtered = [p for p in all_products if MIN_PRICE <= p["price"] <= MAX_PRICE]
    print(f"Подходящих по цене: {len(filtered)}")

    most_expensive = max(filtered, key=lambda p: p["price"]) if filtered else None

    if most_expensive:
        print(f'Самый дорогой: "{most_expensive["name"]}" — ${most_expensive["price"]}')
    else:
        print("Нет подходящих товаров")


if __name__ == "__main__":
    main()