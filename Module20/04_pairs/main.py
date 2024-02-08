# TODO здесь писать код
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = []
for i in range(0, len(numbers)-1, 2):
    pairs.append((numbers[i], numbers[i+1]))

print(f"Оригинальный список: {numbers}")
print(f"Новый список: {pairs}")
print()

#___________________________________________________________________________________
print('Другой способ')
pairs = [(numbers[i], numbers[i+1]) for i in range(0, 10, 2)]

print(f"Оригинальный список: {numbers}")
print(f"Новый список: {pairs}")
print()

#___________________________________________________________________________________
print('Другой способ')
pairs = [(num1, num2) for num1, num2 in zip(numbers[::2], numbers[1::2])]

print(f"Оригинальный список: {numbers}")
print(f"Новый список: {pairs}")
