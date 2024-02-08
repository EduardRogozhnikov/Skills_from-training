shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
while True:
        detail = []
        detail_summ = 0
        detail_name = input("Название детали: ")
        for i in shop:
                for n in i:
                        if detail_name == n:
                                detail.append(i)
        for s in detail:
                detail_summ += s[1]

        print("Кол-во деталей: ", len(detail))
        print("Общая стоимость: ", detail_summ)