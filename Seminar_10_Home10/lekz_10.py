'''
Создайте класс окружность. 
Класс должен принимать радиус окружности при создании экземпляра. 
У класса должно быть два метода, возвращающие длину окружности и её площадь.
'''

'''
import math


class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    def get_length(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_radius(self):
        return self.__radius


if __name__ == '__main__':
    lst = [Circle(), Circle(5)]
    for circle in lst:
        print(f"Длина окружности с радиусом {circle.get_radius()} равна: {circle.get_length()}")
        print(f"Площадь окружности с радиусом {circle.get_radius()} равна: {circle.get_area()}")
'''

'''
import math


class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    def get_length(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


c1 = Circle(10)
print(c1.get_length())
print(c1.get_area())
'''


'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
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


if __name__ == '__main__':
    lst = [Rectangle(), Rectangle(1, 2), Rectangle(3), Rectangle(length=4), Rectangle(width=5)]
    for rectangle in lst:
        print(f"{rectangle} имеет площадь {rectangle.get_area()}")
        print(f"{rectangle} имеет периметр {rectangle.get_perimeter()}")
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


c1 = Rectangle(10, 5)
print(c1.get_length())
print(c1.get_area())
'''



'''
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''

'''
from datetime import datetime as dt


class Person:
    def __init__(self, surname="Anonim", name="Anonim", patronymic="Anonim", age=1,
                 birthday=dt.now().strftime("%d.%m.%Y")):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age
        self.birthdays = self.format_birthday(birthday)

    @staticmethod
    def format_birthday(date):
        try:
            return dt.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
        except Exception as err:
            print("Формат даты указан не верно, принята текущая дата")
            return dt.now().strftime("%d.%m.%Y")

    def get_age(self):
        return self.__age

    def get_fullname(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.get_fullname()}, {self.get_age()} год(а) и день рождения {self.birthdays}"


if __name__ == '__main__':
    print(Person())
    print(Person("Пушкин", "Александр", "Сергеевич", 31, "13.02.1988"))
'''




'''
class Person:
    def __init__(self, full_name, age, height):
        self.full_name = full_name
        self.__age = age
        self.__height = height

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def birthday(self):
        self.__age += 1
        return self.get_age()


p1 = Person('Иванов Иван Иванович', 44, 180)

print(p1.get_age())
print(p1.get_full_name())
print(p1.birthday())
print(p1._Person__height)
'''



'''
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
'''

'''
class Employee(Person):
    def __init__(self, id_="000016", *args, **kwargs):
        self.id = id_
        self.access_level = self.set_access_level()
        super().__init__(*args, **kwargs)

    def set_access_level(self):
        return sum(map(int, self.id)) % 7

    def get_id(self):
        return self.id

    def get_access_level(self):
        return self.access_level

    def __str__(self):
        return super(Employee, self).__str__() + f"id = {self.id}, access_level = {self.access_level}"
'''



'''
class Person:
    def __init__(self, full_name, age, height):
        self.full_name = full_name
        self.__age = age
        self.__height = height

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def birthday(self):
        self.__age += 1
        return self.get_age()


class Employee(Person):
    def __init__(self, full_name, age, height, id):
        super().__init__(full_name, age, height)
        self.id = id

    def get_id(self):
        return self.id

    def get_access_level(self):
        # tmp = 0
        # for i in str(self.id):
        #     tmp += int(i)
        tmp = sum([int(i) for i in str(self.id)])
        return tmp % 7


e1 = Employee('Иванов Иван Иванович', 44, 180, 49)

print(e1.get_age())
print(e1.get_full_name())
print(e1.birthday())

print(e1.get_access_level())
'''



'''
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''

'''
class Horse:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

class Fish:
    def __init__(self, name, age, tail_length):
        self.name = name
        self.age = age
        self.tail_length = tail_length
        
class Bird:
    def __init__(self, name, age, fly_speed):
        self.name = name
        self.age = age
        self.fly_speed = fly_speed
'''


'''
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
'''

'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Horse(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def get_name(self):
        return 'Secret!'

    def get_power(self):
        return self.power


class Fish(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length


class Bird(Animal):
    def __init__(self, name, age, fly_speed):
        super().__init__(name, age)
        self.fly_speed = fly_speed


h1 = Horse('Blacky', 12, 'jump')

print(h1.get_name())
print(h1.get_power())
'''


'''
Решить задачи, которые не успели решить на семинаре.
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
'''