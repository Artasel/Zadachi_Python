'''
num = int(input('Введите год!!! '))

if(num < 1582):
    res = 'Нет календаря'
elif(num % 4 != 0 or num % 100 == 0 and num % 400 != 0):
    res = 'Невысокосный'
else:
    res = 'Высокосный'

print(res)
'''


'''
zv = '*'
prob = ' '

hite = int(input('Введите высоту'))
shir = hite - 1

col_zv = 1

while hite > 0:
    for i in range(shir):
        print(prob, end="")

    for i in range(col_zv):
        print(zv, end="")

    shir -= 1
    col_zv += 2
    hite -= 1
    print()
'''


'''
rows = int(input('Введите количество рядов у елки: '))
symbol = 1
while rows > 0:
    print(' ' * rows, '*' * symbol)
    rows -= 1
    symbol += 2
'''

'''
for i in range(2, 10):
    for j in range(2, 6):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()


print()

for i in range(2, 10):
    for j in range(6, 10):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()
'''

'''
i = 0
while not i in range(1, 1000):
    try:
        i = int(input("Введите число: "))

    except ValueError:
        print("Неверное число")

if i / 10 < 1:
    print(i ** 2)
elif i / 100 < 1:
    print(i // 10 * (i % 10))
elif i / 1000 < 1:
    print(int(f"{i % 10}{i // 10 % 10}{i // 100}"))
'''
import sys
from decimal import *
import math

'''
lister = [12, 'asfd', 12.31]
qwe = {1: 'qwra', 123: 123}
ewq = (12, 42)
qwer = {13, 34, 234, 'sfsf', 23.123}
asd = frozenset([123, 42, 'afa', 34])
data = [1, 'qwe', 1.1, False, lister, qwe, ewq, qwer, asd]


for i, item in enumerate(data, start=1):
    print(f'{i} значение: {item}, адрес: {id(item)}, размер: {sys.getsizeof(item)}')
    if isinstance(item, int) and item > 0:
        print('Является положительным целым числом')

    if isinstance(item, str):
        print('Является строкой')
    
    try:
        print(f'{hash(item)}, это хэш')
    except:
        pass
'''

'''
BINARY = 2
OCTAL = 8


def get_result(num: int, divider: int):
    result = ""
    while num > 0:
        result = str(num % divider) + result
        num //= divider
    return result


num = None
while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f"{bin(num)} == {get_result(num, BINARY)} - двоичное исчисление")
print(f"{oct(num)} == {get_result(num, OCTAL)} - восьмеричное исчисление")
'''

'''
while True:
    num = decimal.Decimal(input('Введите диаметр: '))
    if num <= 1000:
        break
    else:
        print('диаметр должен быть меньше или равен 1000')

rad = num / 2
'''


'''
getcontext().prec = 42 # - Установка точности после запятой

radius: float | None = None
while True:
    try:
        radius = int(input("Введите радиус круга не более 500 и не меньше 1: ")) / 2
        if radius * 2 > 1000 or radius * 2 <= 0:
            raise Exception("Не верный диаметр")
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f"Площадь круга равна: {Decimal(math.pi*radius**2)}")
print(f"Радиус окружности равен: {Decimal(2*math.pi*radius)}")
'''

'''
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. ✔ Используйте комплексные числа
для извлечения квадратного корня.  D=-b+-4ac, D=b**2-4ac
'''
'''
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

d = b**2-4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Корни уравнения,', x1, x2)
elif d == 0:
    print('Корень уравнения =', -b / (2 * a))
else:
    d = complex(b**2-4 * a * c)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('комплексные корни уравнения,', x1, x2)
'''

'''
Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

score = 0
number_of_operations = 0
percentages = 1.5

def replenish(amount: int):
    global score
    global number_of_operations
    global percentages

    print()

    if score >= 5_000_000:
        res = score // 100 * 10
        score -= res
        print('Вычтен налог на богатство 10%: ', res)

    
    if amount % 50 != 0:
        print('Сумма пополнения должна быть кратна 50 у.е.')
        print('Сумма на вашем счете: ', score)
        print('Проценты списания: ', percentages)
    else:
        score += amount
        number_of_operations += 1
        print('Сумма на вашем счете: ', score)
        print('Проценты списания: ', percentages)
    
    if number_of_operations == 3:
        if percentages < 100:
            percentages += 3
        
        number_of_operations = 0


def take_off(amount: int):
    global score
    global number_of_operations
    global percentages

    print()

    if score >= 5_000_000:
        res = score // 100 * 10
        score -= res
        print('Вычтен налог на богатство 10%: ', res)

    if amount % 50 != 0:
        print('Сумма снятия должна быть кратна 50 у.е.')
        print('Сумма на вашем счете: ', score)
        print('Проценты списания: ', percentages)
        return
    elif amount > score:
        print('Недостаточно денег на счете')
        print('Сумма на вашем счете: ', score)
        print('Проценты списания: ', percentages)
        return
    else:
        if amount + amount // 100 * percentages < 30: 
            score -= amount + 30 
            print('Сумма на вашем счете: ', score)
            print('Проценты списания: ', percentages)
        elif amount + amount // 100 * percentages >= 600:
            score -= amount + 600 
            print('Сумма на вашем счете: ', score)
            print('Проценты списания: ', percentages)
        else:
            score -= (amount + amount // 100 * percentages)
            print('Сумма на вашем счете: ', score)
            print('Проценты списания: ', percentages)

    number_of_operations += 1
    if number_of_operations == 3:
        if percentages < 100:
            percentages += 3
        number_of_operations = 0


print('Приветствуем вас в нашем банке!')
while True:
    result = 0
    print()

    try:
        result = int(input('Введите 1 для снятия денег\n\
Введите 2, если хотите положить деньги на счет\n\
Введите 3 для выхода из приложения: '))
    except:
        print("Неверный ввод, требуются цифры: 1, 2 или 3")
    
    if result == 1:
        while True:
            try:
                amounter = int(input("Введите сумму снятия: "))
                break
            except:
                print("Неверный ввод, требуется число")

        take_off(amounter)
    
    if result == 2:
        while True:
            try:
                amounter = int(input("Введите сумму, которую хотите положить на счет: "))
                break
            except:
                print("Неверный ввод, требуется число")

        replenish(amounter)
    
    if result == 3:
        print('Сумма на вашем счете: ', score)
        print('Проценты списания: ', percentages)
        print('Досвидания!!!')
        break