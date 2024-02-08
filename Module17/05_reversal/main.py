# TODO здесь писать код
word = input("Введите строку: ")
first_h = word.index("h")
second_h = word.rindex("h")
print(word[second_h - 1:first_h:-1])




