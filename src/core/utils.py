def get_price(price: str) -> float:
    """Преобразование спаршеной строки(цены) в число."""
    if not price:
        return None
    if '\xa0' in price:
        price = price.replace('\xa0', '')
    if '\nÄ\nруб.' in price:
        price = price.replace('\nÄ\nруб.', '')
    if ',' in price:
        price = price.replace(',', '.')
    if ' ' in price:
        price = ''.join(map(str, price.split()))
    return float(price)