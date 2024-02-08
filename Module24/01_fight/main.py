# TODO здесь писать код
import random


class Warrior:
    def __init__ (self, name, health=100):
        self.name = name
        self.health = health

class Attack:
    def __init__(self, name_1, name_2):
        attacker = random.choice([name_1, name_2])
        defender = name_2 if attacker == name_1 else name_1

        print(f"{attacker.name} атакует {defender.name}")
        defender.health -= 20
        if defender.health < 0:
            health = 0
        print(f"У {defender.name} осталось: {defender.health} здоровья\n")


name_1 = Warrior("Воин 1")
name_2 = Warrior("Воин 2")

while name_1.health > 0 and name_2.health > 0:
    attack_battle = Attack(name_1, name_2)

winner = name_1 if name_2.health == 0 else name_2
print(f"\n{winner.name} одержал победу!\n----------Game Over-----------")
