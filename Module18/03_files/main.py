# TODO здесь писать код
word = input('Введите название файла: ')
if set(word) & set('@№$%^&*()'):
  print('Ошибка: в названии файла запрещенный символ!')
elif word.endswith('.txt') or word.endswith(".docx"):
  print('Файл назван верно!')
else:
  print('Ошибка: неверный формат')