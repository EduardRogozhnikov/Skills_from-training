# TODO здесь писать код
def caaesar_cipher(string, user_shift):
  char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != " " else " ") for sym in string]
  new_stra = ""
  for i_char in char_list:
    new_stra += i_char
  return new_stra

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
stra = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

res = caaesar_cipher(stra,shift)
print("Зашифрованная строка:", res)
