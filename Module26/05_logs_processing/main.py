# TODO здесь писать код
import os


def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


input_file_path = os.path.join('data', 'work_logs.txt')
output_file_path = os.path.join('data', 'output.txt')

if os.path.exists(input_file_path) and not os.path.exists(output_file_path):
    with open(output_file_path, 'w') as output:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
    print("Файл успешно обработан.")
else:
    print("Файлы не найдены или файл вывода уже существует.")
