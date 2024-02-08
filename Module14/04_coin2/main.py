# TODO здесь писать код
def divider (x,y,r):
    if (x <= r and x >= -r) and (y <= r and y >= -r):
      print ("монетка где-то рядом")
    else:
      print ("монетки в области нет")

while True:
    X = float(input("Введите кооринату Х: "))
    Y = float(input("Введите координату У: "))
    radius = int(input("Введите радиус: "))
    divider(X,Y,radius)