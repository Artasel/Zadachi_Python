'''
Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
'''
'''
from typing import Callable

def qwe(func):
    num1 = 0
    num2 = 0
    def wrapper():  # 
        nonlocal num1
        nonlocal num2
        while True:
            try:
                num1 = int(input('Введите число от 1 до 100 для загадывания: '))
                if num1 < 0 or num1 > 100:
                    print('Неверный ввод')
                    continue
            except:
                print('Неверный ввод')
            break
        while True:
            try:
                num2 = int(input('Введите число от 1 до 10 для загадывания: '))
                if num2 < 0 or num2 > 10:
                    print('Неверный ввод')
                    continue
            except:
                print('Неверный ввод')
            break   

        func(num1=num1, num2=num2)
        return
    
    return wrapper

@qwe
def asd(num1=0, num2=0):
    print(f'Угадайте загаданное число за {num2} попыток')
    for i in range(num2):
        z = int(input(f'Вы загадываете число: '))
        if z > num1:
            print('Слишком большое число')
            print(f'Оставшееся число попыток - {num2 - (i + 1)}')
        elif z < num1:
            print('Слишком маленькое число')
            print(f'Оставшееся число попыток - {num2 - (i + 1)}')
        elif z == num1:
            print('Верно!')
            print(f'Оставшееся число попыток - {num2 - (i + 1)}')
            return
    print('Попытки закончились, вы проиграли')
    return

asd()
'''

'''
def get_num(max_value=100):
    while True:
        res = input(f'Введите целое число в диапазоне от 1 до {max_value}: ')
        try:
            res = int(res)
            if res < 1 or res > max_value:
                raise Exception(f'Введённое число не входит в диапазон от 1 до {max_value}, попробуйте ещё раз')
        except Exception as err:
            print(f'Введённое значение не является целым числом в диапазоне от 1 до {max_value}, попробуйте ещё раз')
            continue
        return res


def quiz_num_value(value=None):




    def quiz(quest, attempts):
        while attempts != 0:
            print('Отгадайте число: ')
            ans = get_num(max_value=100)
            if ans == quest:
                return 'Вы угадали'
            if ans > quest:
                print('Не верно, загаданное число меньше')
            else:
                print('Не верно, загаданное число больше')
            attempts -= 1
        return f'Вы проиграли, верный ответ {quest}'

    if value is None:
        print('Введите число для загадывания:')
        value = get_num(max_value=100)

    def quiz_num_attempt(attempt=None):
        if attempt is None:
            print('Введите число количества попыток:')
            attempt = get_num(max_value=10)
        return quiz(value, attempt)

    return quiz_num_attempt


if __name__ == '__main__':
 #   print(quiz_num_value()())
    print(quiz_num_value(10)(5))
'''


'''
import random


def create_guessing_game(answer):
    def guessing_game(attempts):

        for _ in range(attempts):
            guess = int(input('Введите число: '))
            if guess == answer:
                print('Вы угадали число!')
                return
            elif guess < answer:
                print('Число больше!')
            else:
                print('Число меньше!')
        print('Попытки закончились!')

    return guessing_game


num1 = random.randint(1, 100)
num2 = random.randint(1, 10)

create_guessing_game(num1)(num2)
'''


'''
Превратите внешнюю функцию в декоратор. 
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''



'''
import random


def check_data(func):
    def wrapper(answer, attempts):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts <= 10):
            attempts = random.randint(1, 10)
        func(answer, attempts)

    return wrapper


@check_data
def func(answer, attempts):
    print(answer, attempts)

func(553, 350)
# check_data(func)(200, 5)
'''

'''
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове 
файл должен расширяться, а не перезаписываться.Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
'''
'''
import json
import os.path
from os.path import isfile


def save_to_json(func):
    def wrapper(*args, **kwargs):
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', encoding='UTF-8') as f:
                data = json.load(f)
        else:
            data = []
        result = func(*args, **kwargs)
        data.append({'args': args, 'kwargs': kwargs, 'result':result})
        with open(f'{func.__name__}.json','w', encoding='UTF-8') as f:
            json.dump(data,f, indent=4)
    return wrapper
'''

'''
def save_to_json(func):
    def wrapper(*args, **kwargs):
        if os.path.exists(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', 'r') as f:
                dictionary = json.load(f)
        else: 
            dictionary = []
        
        res = func(*args, **kwargs)
        dictionary.append({'args': args, 'kwargs': kwargs, 'result':res})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
            json.dump(dictionary, f, indent=4)
        dictionary = []
        return
    return wrapper



@save_to_json
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    res = sum(args)
    return res


func(11,35,a=1,b=2, c=123)
func(112,352,a=12,b=22, c=1232)
func(113,353,a=13,b=23, c=1233)

with open(f'func.json', 'r') as f:
    json_file = json.load(f)


for name in json_file:
    print(name)
'''

    


'''
Создайте декоратор с параметром. 
Параметр - целое число, количество запусков декорируемой функции.
'''

'''
def run_a_lot(num):
    def run_func(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
            
        return wrapper

    return run_func


@run_a_lot(5)
def func(*args, **kwargs):
    print(args)
    return sum(args)


func(4, 5)
func(3, 6)
'''


'''
Объедините функции из прошлых задач. 
Функцию угадайку задекорируйте:
декораторами для сохранения параметров, 
декоратором контроля значений и 
декоратором для многократного запуска. 
Выберите верный порядок декораторов.


Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
'''


import json
from os.path import isfile
import random
from functools import wraps

# декораторами для сохранения параметров
def save_to_json(func):
    @wraps(func)                  # прячет декораторы от help
    def wrapper(*args, **kwargs):       
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', encoding='UTF-8') as f:
                data = json.load(f)
        else:
            data = []
        result = func(*args, **kwargs)
        data.append({'args': args, 'kwargs': kwargs, 'result': result})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4)

    return wrapper

# декоратором контроля значений
def check_data(func):
    @wraps(func)       # прячет декораторы от help
    def wrapper(answer, attempts):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts <= 10):
            attempts = random.randint(1, 10)
        func(answer, attempts)

    return wrapper

# декоратором для многократного запуска
def run_a_lot(num):
    def run_func(func):
        @wraps(func)   # прячет декораторы от help
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return run_func



@run_a_lot(2)
@save_to_json
@check_data
def guess_game(answer, attempts):
    for _ in range(attempts):
        guess = int(input('Введите число: '))
        if guess == answer:
            print('Угадали!')
            return
        elif guess < answer:
            print('Число больше')
        else:
            print('Число меньше')
    print('Не угадали!')


guess_game(200, random.randint(1, 10))
help(guess_game)