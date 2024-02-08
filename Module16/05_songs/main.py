violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код


count = 1
time_music = 0
new_list = []
num_truck = int(input("Сколько песен выбрать?"))

for num in range (num_truck):
    print("Название", count, "-й песни:", end='')
    music = input(" ")
    for i in violator_songs:
        for new_i in i:
            if new_i == music:
                new_list.append(i)
    count += 1

for n in new_list:
    time_music += n[1]

print("Общее время звучания песен: ", round(time_music,2), "минуты")