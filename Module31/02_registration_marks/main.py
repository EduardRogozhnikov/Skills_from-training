# TODO здесь писать код
import re


lst = input()

result_car = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', lst)
result_taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', lst)

print('Список номеров частных автомобилей:', result_car)
print('Список номеров такси:', result_taxi)