# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть 
# дубликатов.

from random import randint
import itertools

'''
input_list = [randint(0, 10) for _ in range(20)]
print(input_list)

res_list = []

i = 0
while i < len(input_list):
    j = i + 1
    while j < len(input_list):
        if input_list[i] == input_list[j] and input_list[i] not in res_list:
            res_list.append(input_list[i])
            break
        j += 1
    i += 1

print(res_list)
'''

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

'''
text = 'Список - это непрерывная динамическая коллекция элементов. Каждому элементу списка присваивается порядковый \
номер - его индекс. Первый индекс равен нулю, второй - единице и так далее. Основные операции для работы со \
списками - это индексирование, срезы, добавление и удаление элементов, а также проверка на наличие элемента в последовательности.'

text = text.lower()
res_text = ''

for i in text:
    if i not in ['.', ',', '!', '?', '(', ')', '-', '+']:
        res_text += i

text_list = res_text.split()
res_dictionary = {}
text_set = set()
list_num = [10]

for i in text_list:
    text_set.add(i)

x = len(text_set)
while x > 0:
    word = text_set.pop()
    res = 0

    for i in text_list:
        if i == word:
            res += 1

    num_min = min(list_num)

    if len(res_dictionary) < 10:
        res_dictionary.update({word:res})
        list_num.append(res)
    elif res > num_min:
        for name, num in res_dictionary.items():
            if num_min == num:
                res_dictionary.pop(name)
                res_dictionary.update({word:res})
                list_num.remove(num_min)
                list_num.append(res)
                break
    x -= 1

for name, num in res_dictionary.items():
    print(name, num)
'''


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в 
# рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты 
# комплектации рюкзака.

weight = 0
res_list = []
res_list2 = []
def completion_list(lister: list):
    global res_list2
    if lister not in res_list2:
        res_list2.append(lister)


def taking(load_capacity: int) ->list:
    global weight
    global res_list
    global res_list2
    dictionary = \
    {
    'Рюкзак': 2,
    'Палатка': 10,
    'Спальный мешок': 2,
    'Пенка и сидушка': 1,
    'Одежда': 4, 
    'Еда' : 10,
    'посуда': 5,
    'Аптечка': 3,
    'гигиенические принадлежности': 1.5,
    }

    list_names = []
    for names in dictionary.keys():
        list_names.append(names)

    perm_set = itertools.permutations(list_names) # weight

    for i in perm_set:
        for j in i:
            if weight + dictionary[j] <= load_capacity:
                weight += dictionary[j]
                res_list.append(j)
        completion_list(res_list)
        res_list = []
        weight = 0

    print(res_list2)
    
   

taking(6)