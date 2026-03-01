import re
import json


def normalize_price(price_str):
    """
    Convert price like '1 200,00' -> 1200.00 (float)
    """
    cleaned = price_str.replace(" ", "").replace(",", ".")
    return float(cleaned)


def extract_prices(text):
    """
    Extract all final product prices (lines like: 308,00)
    Avoid duplicate extraction from 'Стоимость'
    """
    # Match prices that are alone on a line (like 308,00 or 1 200,00)
    price_pattern = re.findall(r'\n(\d[\d\s]*,\d{2})\nСтоимость', text)
    return price_pattern


def extract_products(text):
    """
    Extract product names.
    They appear after number + dot.
    """
    product_pattern = re.findall(r'\d+\.\n(.+)', text)
    return product_pattern


def extract_datetime(text):
    """
    Extract date and time
    """
    match = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)
    return match.group(1) if match else None


def extract_payment_method(text):
    """
    Extract payment method
    """
    match = re.search(r'(Банковская карта)', text)
    return match.group(1) if match else None


def extract_total(text):
    """
    Extract total amount
    """
    match = re.search(r'ИТОГО:\s*\n([\d\s]+,\d{2})', text)
    return match.group(1) if match else None


def parse_receipt(text):
    products = extract_products(text)
    prices = extract_prices(text)
    total = extract_total(text)
    datetime = extract_datetime(text)
    payment = extract_payment_method(text)

    # Calculate total manually
    numeric_prices = [normalize_price(p) for p in prices]
    calculated_total = sum(numeric_prices)

    result = {
        "products": [
            {"name": name.strip(), "price": prices[i]}
            for i, name in enumerate(products)
        ],
        "total_from_receipt": total,
        "calculated_total": calculated_total,
        "date_time": datetime,
        "payment_method": payment
    }

    return result


if __name__ == "__main__":
    with open("raw.txt", "r", encoding="utf-8") as f:
        receipt_text = f.read()

    parsed = parse_receipt(receipt_text)

    print(json.dumps(parsed, ensure_ascii=False, indent=4))