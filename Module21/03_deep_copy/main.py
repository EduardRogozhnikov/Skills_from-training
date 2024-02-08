import copy   # ))

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код


def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site


numbers_sites = int(input("Сколько сайтов: "))
d_copy = dict()
goods = dict()

for i in range(numbers_sites):
    product_name = input("Введите название продукта для нового сайта: ")
    key = {'title': f'Куплю/продам {product_name} недорого',
           'h2': f'У нас самая низкая цена на {product_name}'}

    for li in key:
        find_key(site, li, key[li])

    name_of_product = f"Сайт для {product_name}:"
    d_copy = copy.deepcopy(site)
    goods[name_of_product] = d_copy

    for key, value in goods.items():
        print(key)
        print(value)
