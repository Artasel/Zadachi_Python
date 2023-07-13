'''
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.
'''

'''
import json
import csv
import pickle
import os
import random
import shutil


os.chdir('Seminar_8_Home_8')
print(os.getcwd())

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
	print(f'{file_name = }')
'''
r'''
def func(name1):
    name2 = 'res.json'

    with open(name1, encoding='UTF-8') as f1, \
            open(name2, 'w', encoding='UTF-8') as f2:
        for line in f1:
            print(json.dumps(line.strip().capitalize()), file=f2)


func('sem7/Test/3.txt')
'''



'''
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
После каждого ввода добавляйте новую информацию в JSON файл. 
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. 
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

'''
def add_to_base():
    name1 = 'res2.json'


    try:
        with open(name1, 'r', encoding='UTF-8') as f1:
            data = json.load(f1)


    except:
        data = {}

    while True:

        name = input('Введите имя: ')
        try:
            access_code = int(input('Введите уровень доступа от 1 до 7: '))
        except:
            continue
        if not 1 <= access_code <= 7:
            continue
        try:
            personal_id = int(input('Введите id: '))
        except:
            continue
        print(data.keys())
        if str(personal_id) in data.keys():
            continue
        break

    data[personal_id] = [name, access_code]
    with open(name1, 'w', encoding='UTF-8') as f1:
        json.dump(data, f1,ensure_ascii=False)

add_to_base()
'''



'''
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''


'''
def json_to_csv(name):
    with open(name,encoding='UTF-8') as f1,\
        open ('res3.csv','w',newline='',encoding='UTF-8') as f2:
            data=json.load(f1)
            rows = []
            for personal_id, value in data.items():
                
                name,level = value
                rows.append({'level': int(level), 'id': int(personal_id), 'name': name})
            csv_write = csv.DictWriter(f2, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
            csv_write.writeheader()
            csv_write.writerows(rows)


json_to_csv('res2.json')
'''




'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Дополните id до 10 цифр незначащими нулями. 
В именах первую букву сделайте прописной. 
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.
'''

'''
def csv_to_json(name):
    with open(name, encoding='UTF-8') as f1, \
            open('res4.json', 'w', encoding='UTF-8') as f2:
        for line in f1.readlines()[1:]:
            data = {}
            level, access_id, name = line.strip().split()
            access_id = f'{int(access_id):010}'
            # print(access_id)
            name = name.capitalize()
            h_name = hash(name + access_id)
            # print(h_name)
            data[h_name] = [level, access_id, name]
            print(json.dumps(data,ensure_ascii=False), file=f2)


csv_to_json('res3.csv')
'''


'''
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
'''


'''
with open('res2.json','r',encoding='UTF-8') as f1:
    with open('res5.pickle','wb') as f2:
        data=json.load(f1)

        pickle.dump(data,f2)
'''



'''
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''



'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку.
'''


