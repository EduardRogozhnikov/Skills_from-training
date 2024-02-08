# TODO здесь писать код

while True:
    password = input('\nПридумайте пароль: ')

    if (sum(letter.isupper() for letter in password) < 1) \
    or (sum(letter.isnumeric() for letter in password) < 3) \
    or (len(password) < 8):
        print('\nПароль ненадёжный. Попробуйте ещё раз.\n') \

    else:
        print('\nЭто надёжный пароль!')
        break