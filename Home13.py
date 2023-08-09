'''
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.
'''

from random import randint

class CheckTriangle(Exception):
	def _init__(self, value):
		self.value = value

	def __str__(self):
		return 'Нельзя создавать треугольник со сторонами отрицательной длины'

'''
a = randint(2, 25)
b = randint(2, 25)
c = randint(2, 25)

'''
a = -4
b = 45
c = 5


if a < 0 or b < 0 or c < 0:
    raise CheckTriangle
if a + b <= c or a + c <= b or b + c <= a:
    print(f'При a = {a}, b = {b}, c = {c} - такого треугольника не существует')
elif a == b == c:
    print(f'При a = {a}, b = {b}, c = {c} - Треугольник равносторонний')
elif a == b or c == b or a == c:
    print(f'При a = {a}, b = {b}, c = {c} - Треугольник равнобедренный')
elif a != b and a != c and b != c:
    print(f'При a = {a}, b = {b}, c = {c} - Треугольник разносторонний')

    