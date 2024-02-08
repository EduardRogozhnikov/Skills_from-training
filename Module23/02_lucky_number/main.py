# TODO здесь писать код
from random import randint

def number_enter(number_ent):
    with open("out_file.txt", "w", encoding="utf=8") as out_file:
        for num in number_ent:
            out_file.write(str(f"{num}, \n"))

def number_enter_text():
    with open("out_file.txt", "r") as out_file_txt:
        print("Содержимое файла out_file.txt: ")
        for ent_txt in out_file_txt:
            print(ent_txt)

number_list = []
number_sum = 0

try:
    while number_sum < 777:
        number = int(input("Введите число: "))

        number_rand = randint(1, 13)
        if number_rand == 13:
            raise BaseException


        number_sum += number
        number_list.append(number)

    print("Вы успешно выполнили условия для выхода из порочного цикла!")



except ValueError:
    print("Требуется число...")
except BaseException:
    print("Вас постигла неудача !")

finally:
    number_enter(number_list)
    number_enter_text()
