# TODO здесь писать код
word = input("Введите слово: ")
list = []
list_2 = []
count = 0
count_word = 0
count_word_2 = 0

for num in word:
    count += 1
ans_word = int(count/2)

for n in word:
    count_word += 1
    list.append(n)
    if count_word == ans_word:
        break

for i in reversed(word):
    count_word_2 += 1
    list_2.append(i)
    if count_word_2 == ans_word:
        break

if list == list_2:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

