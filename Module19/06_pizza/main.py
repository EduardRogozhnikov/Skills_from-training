# TODO здесь писать код
number_of_orders = int(input("Введите кол-во заказов: "))
orders = dict()
for i in range (1, number_of_orders + 1):
    order = input(f"{i} заказ: ").split()
    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] = int(order[2])
        else:
            orders[order[0]][order[1]] = order[2]
    else:
        orders[order[0]] = dict({order[1]: int(order[2])})

for elem_1 in sorted(orders):
    print(f"\n{elem_1}: ")
    for elem_2 in sorted(orders[elem_1]):
        print(f"\t{elem_2}: {orders[elem_1][elem_2]}")





