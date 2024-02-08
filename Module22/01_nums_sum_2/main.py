# TODO здесь писать код
import os

txt_file = open("numbers.txt", "r")
sum_file_numbers = 0
txt_read_file = txt_file.read()
print("Содержимое файла numbers.txt: ")
print(txt_read_file)
txt_file.close()

for i_elem in txt_read_file:
    if i_elem == '2':
        sum_file_numbers += int(i_elem)

print('Содержимое файла answer.txt: ')
print(sum_file_numbers)


