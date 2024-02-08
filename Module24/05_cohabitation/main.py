# TODO здесь писать код
import random


class Person:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 50
        self.home = home

    def eat(self):
        if self.home.food >= 5:
            self.home.food -= 5
            self.satiety += 10
            print(f"{self.name} поел(а).")
        else:
            print(f"{self.name} не может поесть, так как еды недостаточно.")

    def work(self):
        self.satiety -= 5
        self.home.money += 50
        print(f"{self.name} поработал(а).")

    def play(self):
        self.satiety -= 5
        print(f"{self.name} поиграл(а).")

    def go_shopping(self):
        if self.home.money >= 20:
            self.home.money -= 20
            self.home.food += 20
            print(f"{self.name} сходил(а) в магазин за едой.")
        else:
            print(f"{self.name} не может сходить в магазин, так как денег недостаточно.")

    def live(self):
        for day in range(365):
            print(f"\nДень {day + 1}:")
            cube_roll = random.randint(1, 6)

            if self.satiety < 20:
                self.eat()
            elif self.home.food < 10:
                self.go_shopping()
            elif self.home.money < 50:
                self.work()
            elif cube_roll == 1:
                self.work()
            elif cube_roll == 2:
                self.eat()
            else:
                self.play()

            if self.satiety < 0:
                print(f"{self.name} умер(ла) от голода.")
                break


class Home:
    def __init__(self):
        self.food = 50
        self.money = 0


home = Home()
artem = Person("Артем", home)
new_person = input("Кто будет жить в доме ещё? ")
other_person = Person(f"{new_person}", home)

artem.live()
other_person.live()
