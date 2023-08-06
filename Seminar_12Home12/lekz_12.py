'''
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
'''

'''
from collections import defaultdict


class Factorial:
    def __init__(self):
        self._storage = defaultdict(int)

    def __call__(self, value, *args, **kwargs):
        res = 1
        for x in range(1, value + 1):
            res *= x
        self._storage[f'!{value}'] = res
        return res

    def get_all_result(self):
        return self._storage
'''


'''
from collections import deque as deq


class Factorial:
    def __init__(self, k):
        self.max_k = deq(maxlen=k)
        self.values = deq(maxlen=k)

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self.max_k.append(result)
        self.values.append(value)
        return self

    def __str__(self):
        return str({i: j for i, j in zip(self.values, self.max_k)})


f = Factorial(2)
print(f(5))
print(f(7))
print(f(3))
print(f(4))
print(f(2))
'''




'''
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.

'''

'''
from tsk1 import Factorial
import json
from datetime import datetime


class FactorialWithManage(Factorial):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%s")
        with open(f'{filename}.json', 'w', encoding='UTF-8') as f:
            json.dump(self.get_all_result(), f)
'''

'''
from collections import deque as deq
import json
from datetime import datetime as dt


class Factorial:
    def __init__(self, k):
        self.max_k = deq(maxlen=k)
        self.values = deq(maxlen=k)

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self.max_k.append(result)
        self.values.append(value)
        return self

    def __str__(self):
        return str({i: j for i, j in zip(self.values, self.max_k)})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = str(dt.now()).replace(':', '') + '.json'
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(str(self), f)
'''

'''
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''


'''
class FactorialGenerate:
    def __init__(self, *args: int):
        if len(args) == 0:
            raise Exception("InvalidArgument")
        if len(args) == 2:
            start, finish, step = args[0], args[1], 1
        elif len(args) == 1:
            start, finish, step = 1, args[0], 1
        else:
            start, finish, step = args[0], args[1], args[2]
        self.start = start
        self.finish = finish
        self.step = step
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.finish:
            self.result *= self.start
            self.start += self.step
            return self.result
        raise StopIteration
'''


'''
class Factorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = 1
        for i in range(1, start):
            self.result *= i

    def __iter__(self):
        return self

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def __next__(self):
        if self.start < self.stop:
            self.result = self.factorial(self.start)
            self.start += self.step
            return self.result
        else:
            raise StopIteration

    def __str__(self):
        return self.result


for i in iter(Factorial(9, 3, 3)):
    print(i)
'''


'''
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.

'''

'''
class Rectangle:
    def __init__(self, length=None, width=None):
        if length is None and width is None:
            length, width = 1, 1
        elif width is None or length is None:
            width = length if width is None else width
            length = width if length is None else length
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return self.__width * 2 + self.__length * 2

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__width} X {self.__length}"

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
        else:
            print("Результат получается отрицательный, операция не проведена")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Результат получается отрицательный, операция не проведена")
'''

'''
class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('Значение должно быть больше нуля')

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('Значение должно быть больше нуля')
'''

'''
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.

'''

'''
class NewRectangle(Rectangle):
    __slots__ = ['__width', '__length', 'get_area']
'''




'''
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.

'''

'''
class Range:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def validate(self, value):
        if value <= 0:
            raise ValueError('Значение должно быть больше нуля')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Rectangle:
    a = Range()
    b = Range()

    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b
'''



