# TODO здесь писать код
number = int(input("Введите длину списка: "))

list = [(1 if x % 2 == 0
         else x % 5)
        for x in range(number)]

print(list)
