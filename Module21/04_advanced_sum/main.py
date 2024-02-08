# TODO здесь писать код
def sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, int):
            result += arg
        elif isinstance(arg, list):
            result += sum(*arg)
    return result

#print(sum([[1, 2, [3]], [1], 3])) # Ответ: 10
#print(sum(1, 2, 3, 4, 5)) # Ответ: 15