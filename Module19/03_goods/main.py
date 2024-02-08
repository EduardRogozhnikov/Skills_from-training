goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for product in goods:
    magazine = 0
    quantity = ""
    summstock = 0
    for stock in store[goods[product]]:
        magazine += (stock["price"] * stock["quantity"])
        summstock += stock["quantity"]
    if summstock % 10 == 1:
        quantity = str(summstock) + " штука,"
    elif summstock % 10 == 2 or summstock % 10 == 3 or summstock % 10 == 4:
        quantity = str(summstock) + " штуки,"
    else:
        quantity = str(summstock) + " штук,"
    print(product, "-", quantity, "стоимость",
          magazine, "рублей")
