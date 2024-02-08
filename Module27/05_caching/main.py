# TODO здесь писать код
from typing import Callable, Any
import functools


def cash_fib(func: Callable) -> Callable:
    cash = {}

    @functools.wraps(func)
    def res_cash(*args):
        if args not in cash:
            cash[args] = func(*args)
        return cash[args]
    return res_cash


@cash_fib
def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
