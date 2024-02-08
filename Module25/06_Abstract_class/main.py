# TODO здесь писать код
import math


class Shape:
    side_a = 0
    side_b = 0
    square = 0

    def area(self):
        self.square = self.side_a * self.side_b
        return self.square


class Circle(Shape):
    square = 0

    def __init__(self, side_a):
        self.side_a = side_a

    def area(self):
        super().area()
        self.square = math.pi * self.side_a ** 2
        return round(self.square, 2)


class Rectangle(Shape):
    square = 0

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        super().area()
        self.square = self.side_a * self.side_b
        return self.square


class Triangle(Shape):
    square = 0

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        super().area()
        self.square = (self.side_a * self.side_b) / 2
        return self.square


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
