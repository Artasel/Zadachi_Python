'''
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''

'''
import os
from time import time


class AuthorStr(str):

    def __new__(cls, row):
        instance = super().__new__(cls, row)
        instance.user = os.getlogin()
        instance.created_time = time()
        return instance


my_str = AuthorStr("This is testing")
print(my_str)
print(my_str.user)
print(my_str.created_time)
'''



'''
from os import getlogin
from datetime import datetime
from time import time


class MyString(str):
    """
    Данный класс является развитием класса str, который сохраняет информацию кем и когда была создана строка
    """
    def __new__(cls, row):
        instance = super().__new__(cls, row)
        instance.user = getlogin()
        instance.created_time = time()
        instance.created_human = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        return instance


if __name__ == '__main__':
    my_str = MyString("This is testing")
    print(my_str)
    print(my_str.user)
    print(my_str.created_time)
    print(my_str.created_human)
'''



'''
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра

'''

'''
class Archive:
    """
    Данный класс архивирует строки и числа
    """
    _LST_ARCHIVES = []

    def __init__(self, row, num):
        self.row = row
        self.num = num
        self.add_in_lst(self)

    def __str__(self):
        return f"{self.row = } {self.num = }"

    def __str__(self):
        return f"Строка: {self.row}\nЧисло: {self.num}"

    def __repr__(self):
        return f"Archive(row={self.row},num={self.num})"

    @classmethod
    def add_in_lst(cls, object):
        cls._LST_ARCHIVES.append(object)

    @classmethod
    def get_lst_archives(cls):
        return cls._LST_ARCHIVES


if __name__ == '__main__':
    tmp = Archive("tmp1", 1)
    tmp = Archive("tmp2", 2)
    for obj in Archive.get_lst_archives():
        print(obj)
'''



'''
class Archive:
    """
    Данный класс архивирует строки и числа
    """
    list_str = []
    list_int = []

    def __init__(self, int1, str1):
        self.int1 = int1
        self.str1 = str1
        self.list_int.append(int1)
        self.list_str.append(str1)

    def get_int1(self):
        return self.int1

    def get_str1(self):
        return self.str1

    @classmethod
    def get_int_arch(cls):
        return cls.list_int

    @classmethod
    def get_str_arch(cls):
        return cls.list_str


a1 = Archive(42, 'Ответ на все вопросы вселенной')
print(a1.get_int_arch())
print(a1.get_str_arch())
a2 = Archive(43, 'А какой был вопрос?')
print(a2.get_int_arch())
print(a2.get_str_arch())
a3 = Archive(44, 'А какой был вопрос???')
print(a3.get_int_arch())
print(a3.get_str_arch())
print(a3.get_int1())
print(a3.get_str1())
'''


'''
Добавьте к задачам 1 и 2 строки документации для классов.
'''






'''
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя
'''





'''
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
'''

'''
class Rectangle:
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __str__(self):
        return f'{self.p}'

r1 = Rectangle(10)
r2 = Rectangle(5)
print(r1+r2)
print(r2-r1)
'''

'''
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

'''
__eq__(), __ne__(), __lt__(), __le__(), __gt__(), и __ge__()
'''

'''
def __eq__(self, o: object) -> bool:
        return self.get_area() == o.get_area()

    def __ne__(self, o: object) -> bool:
        return self.get_area() != o.get_area()

    def __gt__(self, o: object) -> bool:
        return self.get_area() > o.get_area()

    def __ge__(self, o: object) -> bool:
        return self.get_area() <= o.get_area()

    def __lt__(self, o: object) -> bool:
        return self.get_area() < o.get_area()

    def __le__(self, o: object) -> bool:
        return self.get_area() >= o.get_area()
'''

'''
class Rectangle:
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __str__(self):
        return f'{self.p}'

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p

    def __lt__(self, other):
        return self.p < other.p

    def __le__(self, other):
        return self.p <= other.p

    def __gt__(self, other):
        return self.p > other.p

    def __ge__(self, other):
        return self.p >= other.p


rect1 = Rectangle(4)
rect2 = Rectangle(5)
rect3 = Rectangle(4)

print(rect1 == rect2)  # Output: False
print(rect1 != rect2)  # Output: True
print(rect1 < rect2)  # Output: True
print(rect1 <= rect3)  # Output: True
print(rect1 > rect2)  # Output: False
print(rect1 >= rect3)  # Output: True
'''


'''
class Rectangle:
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p

    def __lt__(self, other):
        return self.p < other.p

    def __le__(self, other):
        return self.p <= other.p

    def __gt__(self, other):
        return self.p > other.p

    def __ge__(self, other):
        return self.p >= other.p

    def __str__(self):
        return f'{self.p}'
'''




'''
Решить задачи, которые не успели решить на семинаре.
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать.
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
'''



class MatrixArray:
    """
    Данный класс создаёт экземпляр двумерной матрицы по полученному массиву, если переданный массив верен
    """

    def __init__(self, matrix):
        if len(set(map(len, matrix))) != 1:
            raise "Данная матрица не возможна"
        self.count_row = len(matrix)
        self.count_col = len(matrix[0])
        self.matrix = matrix

    def __add__(self, other):
        """
        Выполняет сложение двух экземпляров класса, если это возможно
        :param other:
        :return:
        """
        if self.count_row != other.count_row or self.count_col != other.count_col:
            raise "Сложение матриц возможно только в случае одинаковых по количеству строк и столбцов"
        
        new_matrix = []
        for x in range(self.count_row):
            row = []
            for y in range(self.count_col):
                row.append(self.matrix[x][y] + other.matrix[x][y])
            new_matrix.append(row)
        return MatrixArray(new_matrix)

    def __mul__(self, other):
        """
        Выполняет умножение двух экземпляров класса, если это возможно
        :param other:
        :return:
        """
        if self.count_col != other.count_row:
            raise "Операция умножения двух матриц выполнима только в том случае, " \
                  "если число столбцов в первом сомножителе равно числу строк во втором"
        
        new_matrix = []
        for x in range(self.count_row):
            row = []
            for y in range(other.count_col):
                res = 0
                for z in range(self.count_col):
                    res += self.matrix[x][z] * other.matrix[z][y]
                row.append(res)
            new_matrix.append(row)

        return MatrixArray(new_matrix)

    def __str__(self):
        m_ = max([len(str(num)) for el in self.matrix for num in el])
        msg = '\n'.join([' '.join([f"{num:>{m_}}" for num in el]) for el in self.matrix])
        return msg

    def __eq__(self, other):
        return self.matrix == other.matrix


ewq = [[16, 27, 38], [49, 51, 62], [73, 84, 95], [10, 11, 12], [13, 14, 15]]

qwerty = [[16, 27, 38], [49, 51, 62], [73, 84, 95], [10, 11, 12], [13, 14, 15]]


qwe = MatrixArray(ewq)
print(qwe)

print()

ytrewq = MatrixArray(qwerty)
print(ytrewq)

'''
print(qwe.__str__())
print()
print(ytrewq.__str__())
'''
print(qwe.__eq__(ytrewq))