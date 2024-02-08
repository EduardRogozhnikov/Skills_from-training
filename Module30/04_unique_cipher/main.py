# TODO здесь писать код
def count_unique_characters(mes):
    mes = mes.lower()
    unique: int = len(list(filter(lambda x: mes.count(x) == 1, mes)))
    return unique


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
