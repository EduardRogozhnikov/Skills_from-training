# TODO здесь писать код
container_quantity = int(input("Количество контейнеров: "))
container = []
count = 0

for i in range(container_quantity):
    container_n = int(input("Введите вес контейнера: "))
    container.append(container_n)

new_container = int(input("Введите вес нового контейнера: "))
for n in container:
    count += 1
    if n <= new_container:
        number_container = count
        break

print("Номер, который получит новый контейнер: ", number_container)

