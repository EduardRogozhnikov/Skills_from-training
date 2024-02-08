# TODO здесь писать код


def summnumber(number):
    numberONE = 0
    while number > 0:
        numberONE += number % 10
        number //= 10
    print("Сумма чисел: ", numberONE)
    return numberONE
def numberquant (number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    print("Количество цифр в числе: ", count)
    return count

number = int(input("Введите число: "))

summnum = summnumber(number)
numquart = numberquant(number)

print("Разность суммы и количества цифр: ", summnum - numquart)