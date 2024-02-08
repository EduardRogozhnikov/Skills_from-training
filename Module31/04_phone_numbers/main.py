# TODO здесь писать код
import re


numbers = ['9999999999', '999999-999', '99999x9999']
names_list = ['первый номер:', 'второй номер:', 'третий номер:']
for i in numbers:
    if re.fullmatch(r'[8-9]\d{9}', i):
        print(f'{i} : всё в порядке')
    else:
        print(f'{i} : не подходит')
