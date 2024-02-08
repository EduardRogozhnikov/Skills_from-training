# TODO здесь писать код
numbers = []
num = int(input("Введите число: "))

for i in range(1, num + 1, 2):
    numbers.append(i)
print("Список из нечётных чисел от одного до N: ", numbers)
