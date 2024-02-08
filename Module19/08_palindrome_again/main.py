# TODO здесь писать код
def isPoly(string):
    charDict = {}
    for i_sym in string:
        charDict[i_sym] = charDict.get(i_sym, 0) + 1

    od_count = 0
    for i_volue in charDict.values():
        if i_volue % 2 != 0:
            od_count += 1
        return od_count <= 0

string = input("Введите строку: ")
if isPoly(string):
    print("Можно сделать палиндром")
else:
    print("Нельзя сделать палиндромом")
