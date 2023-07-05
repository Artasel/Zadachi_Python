'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

'''
import sys
from datetime import datetime as dt
import calendar


def _leap_year(year: int):
    if calendar.isleap(year):
        print('Год високосный.')
    else:
        print('Год не високосный.')


def check_date(date: str):
    try:
        print(f'{date = }')
        new_date = date.split('.')
        _leap_year(int(new_date[-1]))
        dt.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False

# print(check_date('07.01.1991'))
# print(check_date('07.01.2020'))

if __name__ == '__main__':
    print(check_date(sys.argv[1]))
'''

'''
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8 * 8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи 
не бьют друг друга верните истину, а если бьют - ложь.


Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный 
случайные  варианты и выведите 4 успешных расстановки.
'''

from random import randint as rn


def decision(mass: list):
    iterations = 13
    for i in mass:
        sum = 0
        for j in i:
            sum += j
            if sum > 1:
                return False

    x = 0
    y = 0
    sum = 0
    for _ in range(64):
        if x == 8:
            sum = 0
            x = 0
            y += 1
        for _ in range(1):
            sum += mass[x][y]
            if sum > 1:
                return False
        x += 1

    contain_y = 0
    contain_x = 6
    for _ in range(iterations):
        sum = 0
        x = contain_x
        y = contain_y
        while y < 8 and x < 8:
            sum += mass[x][y]
            if sum > 1:
                return False
            
            x += 1
            y += 1

            if not(y < 8 and x < 8):
                if contain_x != 0:
                    contain_x -= 1
                else:
                    contain_y += 1
    
    contain_x = 6
    contain_y = 7
    for _ in range(iterations):
        sum = 0
        x = contain_x
        y = contain_y
        while contain_y >= x and contain_x <= y:
            sum += mass[x][y]
            if sum > 1:
                return False
            
            x += 1
            y -= 1

            if not(contain_y >= x and contain_x <= y):
                if contain_x != 0:
                    contain_x -= 1
                else:
                    contain_y -= 1
    
    return True


def print_mass(mass: list):
    for i in mass:
        for j in i:
            print(j, end=' ')
        print()


def random_mass():
    amount_success = 0
    while True:
        mass = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

        while True:
            list_coordinates = []
            for _ in range(8):
                list_coordinat_x_y = []
                for _ in range(2):
                    list_coordinat_x_y.append(rn(0, 7))

                a, b = list_coordinat_x_y
                reverse_list_coordinat_x_y = []
                reverse_list_coordinat_x_y.append(b)
                reverse_list_coordinat_x_y.append(a)

                if list_coordinat_x_y not in list_coordinates and reverse_list_coordinat_x_y not in list_coordinates :
                    list_coordinates.append(list_coordinat_x_y)

            if len(list_coordinates) == 8:
                break

        for i in list_coordinates:
                x, y = i
                mass[x][y] = 1

        res = decision(mass)

        if res:
            amount_success += 1
            print_mass(mass)
            print()
        
        if amount_success == 4:
            break


random_mass()


