'''
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать.
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
'''

class Matrix:
    """Этот класс умеет сравнивать, складывать и умножать матрицы"""

    def __init__(self, matrix):
        self.count_row = len(matrix)
        self.count_col = len(matrix[0])
        self.matrix = matrix

       # self.matrix = [[random.randint(10, 99) for i in range(width_matr)] for j in range(height_matr)]

    def __str__(self):
        res = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if j == len(self.matrix[0]) - 1:
                    res += f'{str(self.matrix[i][j])}\n'
                else:
                    res += f'{str(self.matrix[i][j])} '
        return res
    
    def __eq__(self, other):
        return self.matrix == other.matrix
    
    def __mul__(self, other):
        """
        Выполняет умножение двух экземпляров класса
        """
        if self.count_row != other.count_row or self.count_col != other.count_col:
            raise "Умножение матриц возможно только в случае одинаковых по количеству строк и столбцов"


        res_matrix = []
        row = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] * other.matrix[i][j])
            res_matrix.append(row)
        return Matrix(res_matrix)

    def __add__(self, other):
        """
        Выполняет сложение двух экземпляров класса
        """
        if self.count_row != other.count_row or self.count_col != other.count_col:
            raise "Сложение матриц возможно только в случае одинаковых по количеству строк и столбцов"

        res_matrix =[]
        row = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            res_matrix.append(row)
        return Matrix(res_matrix)

   

zaq = [[12, 45, 74], [34, 36, 68], [97, 35, 35]]
qaz = Matrix(zaq)

zaqwe = [[12, 45, 74], [34, 36, 68], [97, 35, 35]]
qwe = Matrix(zaqwe)

zaqwerty = [[12, 45, 74], [34, 36, 68], [97, 35, 35]]
ewq = Matrix(zaqwerty)

res = qwe * ewq + qaz
print(res.__str__())


print()
res = res * qaz
print(res.__str__())

print()


result = qwe + ewq + qaz
print(result.__str__())
