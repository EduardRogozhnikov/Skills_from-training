# TODO здесь писать код
def divition (yearONE, yearsTWO):
    print("Годы от", yearONE, "до", yearsTWO, "с тремя одинаковыми цифрами: ")
    for num in range(yearONE, yearsTWO + 1):
        n1 = num % 10
        n2 = (num // 10) % 10
        n3 = (num // 100) % 10
        n4 = (num // 1000) % 10
        if (n1 == n3 == n4) or (n1 == n2 == n4) or (n2 == n3 == n4) or (n1 == n2 == n3):
            print(num)
year_1 = int(input("Введите первый год: "))
year_2 = int(input("Введите второй год: "))
divition(year_1, year_2)