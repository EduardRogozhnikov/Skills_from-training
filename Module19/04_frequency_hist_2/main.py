# TODO здесь писать код
text = input("Введите текст: ").lower()
frequence = dict()
print("Оригинальный словарь частот: ")
for i in set(text):
    print(f"{i}:{text.count(i)}")
    frequence[text.count(i)] = frequence.get(text.count(i), []) + [i]
print("Инвертированный словарь частот: ")
for ai in frequence:
    print(f"{ai}: {frequence[ai]}")