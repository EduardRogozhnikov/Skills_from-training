# TODO здесь писать код
import functools


def counter(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'Функция {func.__name__} была вызвана {wrapper.count} раз(а)')
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def new_func():
    pass


new_func()
new_func()
new_func()
