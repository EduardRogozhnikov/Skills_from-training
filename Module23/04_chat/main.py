# TODO здесь писать код


user_name = input("Ваше имя? ")
while True:
    print("Увидеть текущий текст чата: '1'\nНаписать сообщение: '2'")
    choice_user = int(input("Введите 1 или 2: "))

    if choice_user == 1:
        try:
            with open("messanger.txt", "r", encoding="utf-8") as messanger_chat:
                messanges = messanger_chat.readlines()
                print("".join(messanges))

        except FileNotFoundError:
            print("Служебное сообщение: файл не найден")

    elif choice_user == 2:
        new_message = input("Введите сообщение: ")
        with open("messanger.txt", 'a', encoding="utf-8") as messanger_chat:
            messanger_chat.write("{name}:{message}\n".
                                 format(name=user_name, message=new_message))

    else:
        print("Неизвестная командра\n")



