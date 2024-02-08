# TODO здесь писать код
import time
import functools
from typing import Callable, Any


def decorator_sleep(func: Callable) -> Callable:
    """Функция задержки на 3 секунды"""

    @functools.wraps(func)
    def sleep_func(*args, **kwargs) -> Any:
        time.sleep(3)
        awakening_func = func(*args, **kwargs)
        return awakening_func
    return sleep_func


@decorator_sleep
def proverka_func():
    """Это для проверки"""
    print("prosto")


proverka_func()
