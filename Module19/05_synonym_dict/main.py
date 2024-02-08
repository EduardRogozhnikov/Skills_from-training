# TODO здесь писать код
sum_word = int(input("Введите количество пар слов: "))
synonyms = dict()
for i in range(1, sum_word + 1):
    word_syn = input(f"{i}, пара: ").lower().split(" - ")
    synonyms[word_syn[0]] = [word_syn[1]]
    synonyms[word_syn[1]] = [word_syn[0]]

while True:
    word = input("\nВведите слово: ").lower()
    if word in synonyms:
        print("Синоним:", str(synonyms[word]))
    else:
        print("Такого слова в словаре нет.")