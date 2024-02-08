# TODO здесь писать код
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += "\t".join(str(element) for element in row)
            result += "\n"
        return result.rstrip("\n")

    def add(self, matrix):
        if self.rows != matrix.rows or self.columns != matrix.columns:
            raise ValueError("Размеры матриц не совпадают.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + matrix.data[i][j]
        return result

    def subtract(self, matrix):
        if self.rows != matrix.rows or self.columns != matrix.columns:
            raise ValueError("Размеры матриц не совпадают.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - matrix.data[i][j]
        return result

    def multiply(self, matrix):
        if self.columns != matrix.rows:
            raise ValueError("Неправильные размеры матриц для умножения.")
        result = Matrix(self.rows, matrix.columns)
        for i in range(self.rows):
            for j in range(matrix.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * matrix.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[j][i] = self.data[i][j]
        return result



# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())