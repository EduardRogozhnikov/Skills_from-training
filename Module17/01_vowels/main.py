# TODO здесь писать код
def func(words):
    vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
    word = [x for x in words for i in vowels if i == x]
    print("Список гласных букв", word)
    print("Длина списка: ", len(word))

while True:
    words = input("Введите текст: ")
    func(words)
    print()
