# TODO здесь писать код
from collections import Counter


def can_be_poly(string):
    return len(string) % 2 == sum(x % 2 for x in Counter(string).values())


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
