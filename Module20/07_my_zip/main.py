# TODO здесь писать код
string_word = "abcd"
numbers_tuple = (10, 20, 30, 40)

generator = ((char, num) for char, num in zip(string_word, numbers_tuple))
print(generator)

for pair in generator:
    print(pair)
