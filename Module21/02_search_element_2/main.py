# TODO здесь писать код
site = {
    'html': {
            'head': {
                    'title': 'Мой сайт'
            },
            'body': {
                    'h2':
                    'Здесь будет мой заголовок',
                    'div': 'Тут, наверное, какой-то блок',
                    'p': 'А вот здесь новый абзац'
            }
    }
}


def find_value(dictionary):
        key = input("Введите искомый ключ: ")
        max_depth = input("Хотите ввести максимальную глубину? Y/N: ")

        if max_depth.lower() == 'y':
                depth = int(input("Введите максимальную глубину: "))
        else:
                depth = None

        def _recursive_find_value(dictionary, target_key, current_depth):
                if current_depth is not None and current_depth < 1:
                        return None

                if isinstance(dictionary, dict):
                        if target_key in dictionary:
                                return dictionary[target_key]
                        else:
                                for value in dictionary.values():
                                        result = _recursive_find_value(value, target_key,
                                                                       current_depth - 1 if current_depth is not None else None)
                                        if result is not None:
                                                return result
                return None

        value = _recursive_find_value(dictionary, key, depth)
        print("Значение ключа:", value)

while True:
        find_value(site)