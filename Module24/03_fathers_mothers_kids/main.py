# TODO здесь писать код
class Parent:
    name = "Алла"
    age = "31 год"
    children = ["Тоня"]
    info_parent = f"Меня зовут {name}, я домохозяйка и мама {children}. Я люблю отдыхать на природе и занимаюсь йогой."


    def lulling(self, сondition, hunger, fatigue, boredom):

        if сondition == 1:
            print(f"Действие: {self.name} готовит еду\n"
                  f"Действие: {self.name} зовет ребенка на кухню..\n"
                  f"Действие: {self.name} кормит ребенка")
            hunger = 100
            return hunger

        elif сondition == 2:
            print(f"Действие: {self.name} берёт ребёнка в руки\n"
                  f"Действие: {self.name} кладёт ребёнка в кровать\n"
                  f"Действие: {self.name} читает сказку\n")
            fatigue = 100
            return fatigue

        elif сondition == 3:
            print(f"Действие: {self.name} читает книгу ребёнку\n"
                  f"Действие: {self.name} обнимает ребенка\n"
                  f"Действие: {self.name} даёт игрушки ребенку\n")
            boredom = 100
            return boredom

        else:
            print(f"Действие: {self.name} занимается йогой\n")

class Children:
    name = "Тоня"
    age = "8 лет"
    hunger = 50
    fatique = 50
    boredom = 50

    def lulling_child (self, hunger, fatique, boredom):
        self.hunger = hunger
        if self.hunger < 50:
            if self.hunger < 0:
                self.hunger = 0
            print(f"# {self.name} голодна")
        else:
            print(f"# {self.name} сыта")

        self.fatique = fatique
        if self.fatique < 50:
            if self.fatique < 0:
                self.fatique = 0
            print(f"# {self.name} устала")
        else:
            print(f"# {self.name} бодрая")

        self.boredom = boredom
        if self.boredom < 50:
            if self.boredom < 0:
                self.boredom = 0
            print(f"# {self.name} скучает")
        else:
            print(f"# {self.name} в спокойном состоянии")


mama = Parent()
child = Children()
while True:
    print("menu:\n 1: Информация о родителе\n"
          "2: Информация о ребенке\n"
          "3: Состояние ребенка")
    menu = int(input("Введите действие '1','2','3': "))

    if menu == 1:
        print(f"Имя: {mama.name}\n"
              f"Возраст: {mama.age}\n"
              f"Дети: {mama.children}\n")
        info_mama = int(input("Рассказать о себе '1', вернуться в меню '2': "))
        if info_mama == 1:
            print(mama.info_parent)

    if menu == 2:
        print(f"Имя: {child.name}\n"
              f"Возраст: {child.age}")

    if menu == 3:
        hunger = child.hunger
        fatique = child.fatique
        boredom = child.boredom
        child.lulling_child(hunger, fatique, boredom)

        menu_child = int(input("Выбрать действие:\n"
                               "1 - покормить\n"
                               "2 - уложить спать\n"
                               "3 - развеселить\n"
                               "4 - отдыхать\n"
                               "'1','2','3','4': "))
        if menu_child == 1:
            child.hunger = mama.lulling(menu_child, hunger, fatique, boredom)
        elif menu_child == 2:
            child.fatique = mama.lulling(menu_child, hunger, fatique, boredom)
        elif menu_child == 3:
            child.boredom = mama.lulling(menu_child, hunger, fatique, boredom)
        else:
            mama.lulling(menu_child, hunger, fatique, boredom)

    child.hunger -= 15
    child.boredom -= 15
    child.fatique -= 15
