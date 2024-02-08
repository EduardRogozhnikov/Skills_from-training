# TODO здесь писать код
video_card = ["3070", "2060", "3090", "3070", "3090"]



count = 5
print("Количество видеокарт: ", count)
for i in range(count):
    print("Видеокарта: ", video_card[i])

print("Старый список видеокарт", video_card)
del video_card[2]
del video_card[3]

print("Новый список видеокарт", video_card)


