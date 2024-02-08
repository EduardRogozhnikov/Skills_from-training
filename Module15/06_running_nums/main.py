# TODO здесь писать код

list = [1,2,3,4,5]
while True:
    print("Список: ", list)
    new_list = []
    count = 0
    motion = int(input("Насколько сдвигать: "))

    for n in reversed(list):
        count += 1
        new_list.append(n)
        if count == motion:
            break
    rest = 5 - motion
    for i in range(1, rest + 1):
        new_list.append(i)

    print("Изначальный список ", list)
    print("Новый список: ", new_list)
    list = new_list
    print()


