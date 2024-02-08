# TODO здесь писать код
"""
Документация к коду:
1. worth - стоимость аргумента
2. tax_worth - вычисляется сумма налога на аргумент
3. tax - налог (переносится из подкласса в основной класс)
4. type_arg - сам аргумент (переносится из подкласса в основной класс)

Функция в основном классе payment - выводит в терминале на какой аргумент какой налог.
"""


class Property:
    tax = None
    type_arg = None

    def __init__(self, worth):
        self.worth = worth
        self.tax_worth = self.worth * self.tax

    def payment(self):
        print(f"Налог на {self.type_arg} = {round(self.tax_worth, 1)}")


class Apartment(Property):
    tax = 1/1000
    type_arg = "apartment"


class Car(Property):
    tax = 1/200
    type_arg = "car"


class CountryHouse(Property):
    tax = 1/500
    type_arg = "dacha"


while True:
    money = int(input("Сколько у вас денег: "))
    car_worth = int(input("Сколько стоит машина: "))
    apartment_worth = int(input("Сколько стоит дом: "))
    country_house_worth = int(input("Сколько стоит дача: "))

    car = Car(car_worth)
    apartment = Apartment(apartment_worth)
    country_house = CountryHouse(country_house_worth)
    car.payment()
    apartment.payment()
    country_house.payment()

    summ_tax = car.tax_worth + apartment.tax_worth + country_house.tax_worth
    if money >= summ_tax:
        money -= summ_tax
        print("Вы оплатили все налоги!\nМолодец, встретимся в следующем экономическом году...")

    else:
        print(f"У вас не хватает {round(summ_tax - money, 1)} для оплаты налогов...\n"
              f"Пополните счет и повторите попытку!")
