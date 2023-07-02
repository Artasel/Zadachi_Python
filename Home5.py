'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх 
элементов: путь, имя файла, расширение файла.
'''


def func(text: str)->tuple:
    list_way = text.split('\\')
    cont_list = []

    cont_list = list_way[-1].split('.')
    list_way.pop()
    list_way.extend(cont_list)
    
    *way, name_file, expansion = list_way
    res_tuple = way, name_file, expansion

    return res_tuple


way = r'C:\Users\Tarona\Desktop\Zadachi_Python\Home4.py'

print(func(way))



'''
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием 
процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается 
как ставка умноженная на процент премии.
'''
'''
from decimal import *

getcontext().prec = 42

list_name = ['Алексей', 'Борис', 'Всеволод', 'Катерина', 'Виктор', 'Владислав', 'Павел']
list_bet = [10000, 11000, 12000, 13000, 14000, 15000, 16000]
list_prize = ['30.50%', '25.75%', '20.60%', '15.12%', '10.25%', '5.56%', '3.90%']
'''

'''
list_prize_res = []
for i in list_prize:
    container = i[:len(i) - 1]
    list_prize_res.append(Decimal(container))

list_list_bet = []
for i in range(len(list_prize_res)):
    list_list_bet.append(Decimal(list_bet[i]) + Decimal(list_bet[i]) / 100 * list_prize_res[i])

res_dict = {}
for i in range(len(list_name)):
    res_dict[list_name[i]] = list_list_bet[i]
'''

#for i, j in res_dict.items():
#    print(f'{i} => {j}')


# dict_res = {print(f'{key} => {value}') for (key,value) in res_dict.items()}



'''
def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: Decimal]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (Decimal(i[:-1]) for i in bonus))}.items()


print(*(salary_gen(list_name, list_bet, list_prize)))
'''

'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).  rsplit
'''
'''
def fib_func(num: int):
    x, y = 0, 1
    for _ in range(num):
        yield x
        x, y = y, x + y


qwe = fib_func(12)

print(*qwe)
'''