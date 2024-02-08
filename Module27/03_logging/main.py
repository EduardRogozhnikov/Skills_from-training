# TODO здесь писать код
from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор, логирующий функции.
    Если во время выполнения декорируемой функции возникла ошибка,
    то в файл function_errors.log записываются название функции и ошибки.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'\nНазвание функции: {func.__name__}.'
              f'\nДокументация:{func.__doc__}')

        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            with (open('function_errors.log', 'a+', encoding='utf-8') as file_error):
                file_error_messege = (f'{now} Название функции: [{func.__name__}].'
                                      f'Исключение: [{type(error).__name__}]. Ошибка: [{error}]\n')
                file_error.write(file_error_messege)
                print(file_error_messege)

    return wrapped_func


@logging
def first_func() -> int:
    """ Функция запрашивает ввод целочисленного числа. """
    number_int = int(input('Введите число: '))
    return number_int


@logging
def second_func() -> int:
    """ Функция выводит результат деления 10 на введенное пользователем число. """
    number_int = int(input('Введите число: '))
    result = 10 // number_int
    print(f"Ответ: {result}")
    return result


@logging
def third_func() -> None:
    """ Функция выводит текст сообщения. """
    print('Сообщение: функция с сообщением.')


while True:
    first_func()
    second_func()
    third_func()

    close = input("Хотите закрыть цикл?\n (Y/N): ")
    if close == "Y" or close == "y":
        print("Программа завершена.")
        break

