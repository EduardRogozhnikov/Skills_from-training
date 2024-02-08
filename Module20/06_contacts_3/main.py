# TODO здесь писать код
def contact (new_contact):
    string_contact = tuple(new_contact.split(','))

def search_contact(last_name, contacts):
    for name, number in contacts.items():
        if name[1] == last_name:
            return name[0] + " " + name[1] + " " + str(number)
    return "Контакт не найден"

contact_book = {}
while True:
    print("Введите номер действия: ")
    print("   1. Добавить контакт")
    print("   2. Найти человека")
    number_action = int(input(">>> "))

    if number_action == 1:
        new_contact = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").split())
        number_phone = int(input("Введите номер телефона: "))
        contact_book[new_contact] = number_phone
        print("Текущий словарь контактов: ", contact_book)
        print()

    elif number_action == 2:
        key_contact = input("Введите фамилию для поиска: ")
        result = search_contact(key_contact, contact_book)
        print(result)
        print()

    else:
        print("Неккоректный ввод, повторите попытку.")
        print()
        print()
        print()
