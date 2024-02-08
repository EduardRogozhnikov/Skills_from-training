# TODO здесь писать код
IP = input("Введите IP: ").split(".")
result = "IP - aдрес корректен."

if len(IP) != 4:
    result = "Адрес — это четыре числа, разделённые точками."
else:
    for i in range(4):
        if IP[i].isdigit() == False:
            result = f"{IP[i]} - это не целое число."
        elif not 0 <= int(IP[i]) <= 255:
            result = f"{IP[i]} не попадает в диапазон 0 - 255"
print(result)


