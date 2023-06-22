# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex 
# используйте для проверки своего результата.
# В шестнадцатеричной записи числа 10, 11, 12, 13, 14, 15 записываются буквами A, B, C, D, E, F соответственно.

'''
hexadecimalS = 16
diction = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

def get_result(num: int, divider: int):
    result = ""
    while num > 0:
        res = num % divider
        if res in diction:
            result = diction[res] + result
        else:
            result = str(res) + result
        num //= divider
    return result

while True: 
    try:
        number = int(input("Введите число: "))
        break
    except:
        print("Неверный ввод, требуется число")

print(f'{get_result(number, hexadecimalS)} == {hex(number)[2:]}')
'''

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions
import math


def string_work_1(text: str):
    number = ''
    
    for i in range(len(text)):
        if text[i].isdigit():
            number += text[i]
        elif not text[i].isdigit():
            return int(number)
        
def string_work_2(text: str):
    check = False
    number = ''
    
    for i in range(len(text)):
        if not text[i].isdigit():
            check = True
        if text[i].isdigit() and check:
            number += text[i]
    return int(number)


def nods_1(num_1: int, num_2: int) -> str:
    while True:
        nod = math.gcd(num_1, num_2)
        num_1 = num_1 // nod
        num_2 = num_2 // nod
        if nod == 1:
            break
    return str(num_1)

def nods_2(num_1: int, num_2: int) -> str:
    while True:
        nod = math.gcd(num_1, num_2)
        num_1 = num_1 // nod
        num_2 = num_2 // nod
        if nod == 1:
            break
    return str(num_2)


def example(first: str, second: str, sign: str):
    number_1 = string_work_1(first)
    number_2 = string_work_2(first)
    number_3 = string_work_1(second)
    number_4 = string_work_2(second)

    if number_2 == 0 or number_4 == 0:
        print('Знаменатель не может быть равен 0')   
        return

    if sign == '-':
        if number_2 == number_4:
            result = number_1 - number_3

            f1 = fractions.Fraction(number_1, number_2)
            f2 = fractions.Fraction(number_3, number_4)
            res_frac = f1 - f2

            result_2 = nods_1(result, number_2)
            number_2 = nods_2(result, number_2)

            result_2 += '/' + number_2 + ' == ' + str(res_frac)
            return result_2
        else:
            f1 = fractions.Fraction(number_1, number_2)
            f2 = fractions.Fraction(number_3, number_4)
            res_frac = f1 - f2

            result = number_1 * number_4 - number_2 * number_3
            result_2 = number_2 * number_4

            result_3 = nods_1(result, result_2)
            result_2 = str(nods_2(result, result_2))

            result_3 += '/' + result_2 + ' == ' + str(res_frac)
            return result_3
    
    if sign == '+':
        if number_2 == number_4:
            result = number_1 + number_3

            f1 = fractions.Fraction(number_1, number_2)
            f2 = fractions.Fraction(number_3, number_4)
            res_frac = f1 + f2

            result_2 = nods_1(result, number_2)
            number_2 = nods_2(result, number_2)

            result_2 += '/' + number_2 + ' == ' + str(res_frac)
            return result_2
        else:
            f1 = fractions.Fraction(number_1, number_2)
            f2 = fractions.Fraction(number_3, number_4)
            res_frac = f1 + f2

            result = number_1 * number_4 + number_2 * number_3
            result_2 = number_2 * number_4

            result_3 = nods_1(result, result_2)
            result_2 = nods_2(result, result_2)

            result_3 += '/' + result_2 + ' == ' + str(res_frac)
            return result_3
        
    if sign == '*':
        f1 = fractions.Fraction(number_1, number_2)
        f2 = fractions.Fraction(number_3, number_4)
        res_frac = f1 * f2

        result = number_1 * number_3
        result_2 = number_2 * number_4

        result_3 = nods_1(result, result_2)
        result_2 = nods_2(result, result_2)

        result_3 += '/' + result_2 + ' == ' + str(res_frac)
        return result_3
    
    if sign == '/':
        if number_3 == 0:
            print('Второй числитель не может быть равен 0 при делении')   
            return
        f1 = fractions.Fraction(number_1, number_2)
        f2 = fractions.Fraction(number_3, number_4)
        res_frac = f1 / f2

        result = number_1 * number_4
        result_2 = number_2 * number_3

        result_3 = nods_1(result, result_2)
        result_2 = nods_2(result, result_2)

        result_3 += '/' + result_2 + ' == ' + str(res_frac)
        return result_3

qwe = '23/23'
ewq = '654/42'

print(example(qwe, ewq, '/'))