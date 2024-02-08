# TODO здесь писать код


def divider(num):

    i = 1

    while i <= num:
        i=i + 1
        if num % i == 0:
            print ("Наименьший делитель, отличный от единицы: ", i)
            break


number = int(input("Введите число: "))
divider(number)
