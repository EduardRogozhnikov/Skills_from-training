# TODO здесь писать код
def num_func_recurs(num):
    if num <= 0:
        return 1
    num_func_recurs(num - 1)
    print(num)


number = int(input("Введите num: "))
num_func_recurs(number)