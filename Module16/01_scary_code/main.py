# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу
list_one = [1, 5, 3]
list_two = [1, 5, 1, 5]
list_tree = [1, 3, 1, 5, 3, 3]
count_five = 0
count_tree = 0

for i in list_two:
    list_one.append(i)
for i in list_one:
    if i == 5:
        count_five += 1
        del list_one[list_one.index(i)]
print("Кол-во цифр 5 при первом объединении: ", count_five)

for i in list_tree:
    list_one.append(i)
for i in list_one:
    if i == 3:
        count_tree += 1
print("Кол-во цифр 3 при втором объединении: ", count_tree)

print("Итоговый список: ", list_one)