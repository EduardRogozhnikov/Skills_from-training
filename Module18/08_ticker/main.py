# TODO здесь писать код
first_s = input('Введите первую стоку: ')
second_s = input('Введите вторую строку: ')

if first_s == second_s:
    print('Строки идентичны')
else:
    k = second_s.index(second_s[0]) + first_s.index(second_s[0])
    for position in range(len(second_s)):
        if second_s[position] != first_s[(position + k) % len(second_s)]:
            print('Первую строчку нельзя получить из второй методом циклического сдвига')
            break
    else:
        print('Первую строчку можно получить из второй со сдвигом в ', k)