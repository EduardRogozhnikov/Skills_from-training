# TODO здесь писать код
def compression (text):
    counter = 1
    compress = []

    for symb in range(len(text)):
        if text[symb] == text [symb + 1: symb + 2]:
            counter += 1
            continue
        compress.append(text[symb] + str(counter))
        counter = 1

    return compress

text = input("Введите строку: ")
print("Закодированная строка: {}".format("".join(compression(text))))