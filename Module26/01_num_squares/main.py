# TODO здесь писать код
# Способ №1 класс-итератор
class SquareIterator:
    def __init__(self, numb):
        self.current = 1
        self.numb = numb

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.numb:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


number = int(input("Введите число N: "))
iterator = SquareIterator(number)
for num in iterator:
    print(num)


# Способ №2 функция-генератор
def square_generator(numb):
    current = 1
    while current <= numb:
        yield current ** 2
        current += 1


number = int(input("Введите число N: "))
generator = square_generator(number)
for num in generator:
    print(num)


# Способ №3 генераторное выражение
number = int(input("Введите число N: "))
squares = (x ** 2 for x in range(1, number + 1))
for num in squares:
    print(num)
