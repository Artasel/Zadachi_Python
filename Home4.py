'''
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) 
на None. 
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''

'''
def work_with_s(*args: str):
    res_list = []

    for i in args:
        if i.endswith('s') and len(i) > 1:
            res_list.append('None')
        else:
            res_list.append(i)

    return res_list


first = 'serhcsczs'
second = 'vdfvbgdvs'
third = 'gdbvsrzcd'
fourth = 'cbhcghb'
fifth = 's'

print(work_with_s(first, second, third, fourth, fifth))



eggs = 5
tomatoes = 10
potatoes = 3
sugar = 2
s = 34

def replace_s_vars():
    for var_name in list(globals()):
        if var_name != "s" and var_name.endswith("s"):
            globals()[var_name[:-1]] = globals()[var_name]
            del globals()[var_name]
            globals()[var_name] = None


replace_s_vars()
print(eggs, egg) # переменная egg создалась через globals  хотя и не обьявляясь в коде
'''




'''
Напишите функцию для транспонирования матрицы
'''

'''
def transposition(matr, new_width, new_height):
    max_width_heigh = len(matr) * len(matr[0])
    trans_matr = []
    lister = []

    if new_height * new_width != max_width_heigh:
        return 'Введены некоректные данные'
    
    if new_width == len(matr[0]):
        return matr
    
    lister.append(len(matr) - 1)
    lister.append(len(matr[0]) - 1)
    lister.append(len(matr) + 1)
    lister.append(len(matr[0]) + 1)
    
    if new_height in lister and new_width in lister or new_width == new_height: 
        zip_matr = zip(*matr)
        trans_matr = [list(row) for row in zip_matr]
        return trans_matr
    

    num_list =[]
    for i in range(len(matr[0])):              # ширина
        for j in range(len(matr)):             # высота
            if len(num_list) < new_width:      # если список меньше ширины
                num_list.append(matr[j][i])    # ложим в список сверху вниз
            if len(num_list) == new_width:     # если список равен ширине
                trans_matr.append(num_list)    # ложим в результирующий список, обычный список
                num_list =[]                   # обнуляем обычный список
    
    return trans_matr




m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

print(transposition(m, 5, 4))
'''

'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
'''

'''
def dict_work(**kwargs)->dict:
    res_dict = {}
    for name, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        res_dict[value] = name
    
    return res_dict


print(dict_work(x = 123, y = 'qwe', c = [43, 45, 7], d = -0.5, e = {'qwe': 132, 'ewq': 54}, f = {12, 54, 45}))
'''



'''
Возьмите задачу о банкомате из семинара 2. Разбейте её 
на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

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
list_replenish_take_off = []

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
        text = f'Записано на счет: {amount}'
        list_replenish_take_off.append(text)
    
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
            text = f'Списано со счета: {amount}'
            list_replenish_take_off.append(text)
        elif amount + amount // 100 * percentages >= 600:
            score -= amount + 600 
            print('Сумма на вашем счете: ', score)
            print('Проценты списания: ', percentages)
            text = f'Списано со счета: {amount}'
            list_replenish_take_off.append(text)
        else:
            score -= (amount + amount // 100 * percentages)
            print('Сумма на вашем счете: ', score)
            print('Проценты списания: ', percentages)
            text = f'Списано со счета: {amount}'
            list_replenish_take_off.append(text)

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
        print(list_replenish_take_off)
        print('Досвидания!!!')