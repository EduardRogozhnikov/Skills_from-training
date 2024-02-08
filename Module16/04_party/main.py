
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
while True:
    print("Сейчас на вечеринке", len(guests), "человек: ", guests)
    doing = input("Гость пришёл или ушёл? ")

    if doing == "пришёл" or doing == "пришел":
        name_guest = input("Имя гостя: ")
        if len(guests) < 6:
            print("Привет, ", name_guest + "!")
            guests.append(name_guest)
        else:
            print("Прости, ", name_guest + ", но мест нет.")

    elif doing == "ушёл" or doing == "ушел":
        name_guest = input("Имя гостя: ")
        for i in guests:
            if i == name_guest:
                indx = guests.index(i)
                print("Пока, ", i + "!")
                del guests[indx]

    elif doing == "Пора спать" or doing == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break

    print()
    print()