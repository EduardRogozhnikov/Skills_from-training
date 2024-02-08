# TODO здесь писать код
def counting(mem_list, number, start):
    shift = 0
    while len(mem_list) != 1:
        print(f"\nТекущий круг людей{mem_list}")
        print(f"Начало счета с номера{start}")

        out_number_index = abs(round(number % len(mem_list))) - 1 + shift
        print(f"Выбывает человек под номером {mem_list[out_number_index]}")
        mem_list.remove(mem_list[out_number_index])
        if out_number_index == len(mem_list):
            start = mem_list[0]
        else:
            start = mem_list[out_number_index]
        shift = mem_list.index(start)

    print(f"\nОстался человек под номером {mem_list[0]}")


members = int(input("Кол-во человек: "))
key_number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {key_number}-й человек")

members_list = list(range(1, members + 1))
start_number = 1


counting(members_list, key_number, start_number)