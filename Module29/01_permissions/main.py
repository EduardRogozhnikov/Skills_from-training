# TODO здесь писать код
from typing import Callable
import functools
from collections.abc import Callable


def check_permission(user: str) -> Callable:
    def decor_func(func: Callable) -> Callable:

        @functools.wraps(func)
        def func_decor_permission(*args, **kwargs):
            try:
                if user in user_permissions:
                    func()
                else:
                    raise PermissionError("PermissionError")
            except PermissionError as ex:
                print(f"{ex}: у пользователя недостаточно прав, "
                      f"чтобы выполнить функцию {func.__name__}")

            return func

        return func_decor_permission

    return decor_func


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
