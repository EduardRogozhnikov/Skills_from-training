# TODO здесь писать код
import random
list_one = [round(random.uniform(5, 10), 2) for i in range(20)]
list_two = [round(random.uniform(5, 10), 2) for i in range(20)]
list_tree = [list_one[n] if (list_one[n] > list_two[n]) else list_two[n] for n in range(20)]
print("Первая команда: ", list_one)
print('Вторая команда: ', list_two)

print('Победители тура: ', list_tree)
