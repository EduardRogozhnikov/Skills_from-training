# TODO здесь писать код
def validate_data(data):
    name, email, age = data.split()

    # Проверка на наличие всех трех полей
    if len(name) == 0 or len(email) == 0 or len(age) == 0:
        raise IndexError("НЕ присутствуют все три поля")

    # Проверка поля "Имя" на наличие только букв
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")

    # Проверка поля "Имейл" на наличие @ и точки
    if "@" not in email or "." not in email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")

    # Проверка поля "Возраст" на диапазон от 10 до 99
    if not 10 <= int(age) <= 99:
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")


def process_registrations(file):
    good_file = open("registrations_good.log", "w", encoding="utf-8")
    bad_file = open("registrations_bad.log", "w", encoding="utf-8")

    with open(file, "r", encoding="utf-8") as file_reg:
        for line in file_reg:
            try:
                validate_data(line.strip())
                good_file.write(line)
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                bad_file.write(f"{line.strip()}        {str(e)}\n")

    good_file.close()
    bad_file.close()

    with open("registrations_bad.log", "r", encoding="utf-8") as bad_file:
        print("Содержимое файла registrations_bad.log:")
        for i in bad_file:
            print(i.strip())

    with open("registrations_good.log", "r", encoding="utf-8") as good_file:
        print("\nСодержимое файла registrations_good.log:")
        for g in good_file:
            print(g.strip())


process_registrations("registrations.txt")

