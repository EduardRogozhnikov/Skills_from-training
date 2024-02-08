# TODO здесь писать код
# import os
#
# def get_directory_size_and_count(path):
#     total_size = 0
#     num_files = 0
#     num_dirs = 0
#
#     for root, dirs, files in os.walk(path):
#         num_dirs += len(dirs)
#         num_files += len(files)
#
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 total_size += os.path.getsize(file_path)
#
#     return total_size, num_files, num_dirs
#
# directory_path = input("Введите путь к каталогу: ")
# size, num_files, num_dirs = get_directory_size_and_count(directory_path)
#
# size_kb = size / 1024
#
# print(directory_path)
# print(f"Размер каталога (в Кб): {size_kb:.6f}")
# print(f"Количество подкаталогов: {num_dirs}")
# print(f"Количество файлов: {num_files}")

import os


def file_sizes(path):
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_list = open('all_files.txt', 'a')
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = str(os.path.getsize(file_path)) + '\n'
            file_list.write(file_size)
            file_list.close()
        else:
            file_sizes(os.path.abspath(os.path.join(path, i_elem)))


def dir_count(path):
    count = 0
    for i_elem in os.listdir(path):
        if os.path.isdir(os.path.abspath(os.path.join(path, i_elem))):
            count += 1
    return count


def total_file_sizes(path):
    my_list = []
    total_size = 0
    total_files = 0
    for i_elem in path:
        total_size += int(i_elem)
        total_files += 1
    my_list.append(total_files)
    my_list.append(total_size / 1024)

    return my_list


path_request = input("Введите путь: ")
path = os.path.abspath(os.path.join('..', '..', path_request))

file_sizes(path)
all_files = open('all_files.txt', 'r')
my_list = total_file_sizes(all_files)
all_files.close()
os.remove('all_files.txt')

print('Размер каталога (в Кб):', my_list[1])
print('Количество файлов:', my_list[0])
print('Количество подкаталогов:', dir_count(path))
