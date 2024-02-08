# TODO здесь писать код
import os

with open("zen.txt", "r") as file:
    lines = file.readlines()  # Читаю все строки и сохраняю их в переменной


for line in reversed(lines):
    print(line.rstrip())  # Я так понял rstrip() удаляет лишнее и делает красоту
