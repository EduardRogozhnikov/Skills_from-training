# TODO здесь писать код
name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
new_name_one = []
new_name_two = []

for i in range(0,8,2):
    new_name_one.append(name[i])
for i in range(1,8,2):
    new_name_two.append(name[i])

print("Первый день: ", new_name_one)
print("Второй день: ", new_name_two)
