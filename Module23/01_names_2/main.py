# TODO здесь писать код
def func_except_file(except_in_code):
    with open("errors.log", "a", encoding="utf-8") as error_file_txt:
        error_file_txt.write(except_in_code + "\n")


line_count = 0
people_sym_sum = 0

try:
    with open("people.txt", "r", encoding="utf-8") as people_text:
        for people in people_text:
            line_count += 1
            people_sum = len(people.strip())

            if people_sum < 3:
                except_code = f"Ошибка: менее трёх символов в строке {line_count}."
                print(except_code)
                func_except_file(except_code)

            people_sym_sum += people_sum

except FileNotFoundError:
    func_except_file("Файл people.txt не найден.")
finally:
    print(f"Общее количество символов: {people_sym_sum}.")



