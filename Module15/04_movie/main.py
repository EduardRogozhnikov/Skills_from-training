films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
#TODO здесь писать код
like_films = []
sum_like_films = int(input("Сколько добавить фильмов: "))
for i in range(sum_like_films):
    films_name =  input("Введите название фильма: ")
    for n in films:
        if films_name == n:
            like_films.append(films_name)
            mist = 1
            break
    if mist != 1:
        print("Фильма", films_name, "у нас нет :(")
    mist = 0

print()
print("Ваш список любимых фильмов: ", like_films)
