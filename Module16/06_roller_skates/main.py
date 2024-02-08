# TODO здесь писать код
while True:
    skates = []
    people = []
    people_skates = 0
    count_s = 1
    count_p = 1

    skates_count = int(input("Кол-во коньков: "))
    for num in range(skates_count):
        print("Размер", count_s, "-й пары:", end="")
        skates_num = int(input(""))
        skates.append(skates_num)

    print()
    people_count = int(input("Кол-во людей: "))
    for num in range(people_count):
        print("Размер ноги", count_s, "-го человека:", end="")
        people_num = int(input(""))
        people.append(people_num)

    for p in people:
        for s in skates:
            if p == s:
                indx = skates.index(s)
                del skates[indx]
                people_skates += 1

    print()
    print("Наибольшее кол-во людей, которые могут взять ролики: ", people_skates)

    print("|" + "-" * 10 + "|")
    print("|Завершить?|", end=" ")
    off = input(" ")
    if off == "Да" or off == "да":
        print("|" + "-" * 10 + "|")
        print()
        print("|" + "-" * 10 + "|")
        print("|Завершено!|")
        print("|" + "-" * 10 + "|")
        break
    else:
        print("|" + "-" * 10 + "|")
        print()
        print("|" + "-" * 11 + "|")
        print("|Продолжаем!|")
        print("|" + "-" * 11 + "|")
    print()
    print()
    print()