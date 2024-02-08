# TODO здесь писать код
from typing import List
import functools


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_second: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
print("Новый список floats:\n", floats_second)
names_second: List[str] = list(filter(lambda x: len(set(x)) >= 5, names))
print("Новый список names:\n", names_second)
numbers_second = (functools.reduce(lambda x, y: x * y, numbers))
print("Новый список numbers:\n", numbers_second)
