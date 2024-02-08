# TODO здесь писать код

# Здесь создайте функцию get_sage_sqrt
import math


def get_sage_sqrt(num):
    try:
        if type(num) == str:
            raise TypeError("Невозможно вычислить квадратный корень из строки")
        elif num > 0:
            sqrt_num = math.sqrt(num)
            return sqrt_num
        elif num < 0:
            raise ValueError("Нельзя вычислить квадратный корень из отрицательного числа")
        elif num == 0:
            raise ValueError("Число 0 некорректный аргумент")
        else:
            raise Exception("Некорректный аргумент")

    except TypeError as exc:
        return exc
    except ValueError as exc:
        return exc
    except Exception as exc:
        return exc


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
