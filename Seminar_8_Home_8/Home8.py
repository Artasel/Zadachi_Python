'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните 
в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами разных форматов.
'''
'''
from pathlib import Path
import csv
import json
import pickle
import os


def get_dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def direct_info(direct: Path):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with open('direct_info.json', 'w') as f_json, \
            open('direct_info.csv', 'w', newline='', encoding='utf-8') as f_csv,\
            open('direct_info.pickle', 'wb') as f_pickle:
        
        for dir_path, dir_name, file_name in os.walk(direct): # обход переданной директории
            json_data.setdefault(dir_path, {})  # в словарь помещается путь в качестве ключа, с пустым значением

            for dir in dir_name:
                size = get_size(dir_path + '/' + dir)   # получает размер директории
                json_data[dir_path].update({dir: {'size': size, 'file_or_dir': 'directory'}}) # кладет в значение словаря новый словарь
                rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'}) # кладет в список новый словарь

            for fi in file_name:
                size = get_size(dir_path + '/' + fi) # получает размер файла
                json_data[dir_path].update({fi: {'size': size, 'file_or_dir': 'file'}}) # кладет в значение словаря новый словарь
                rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_dir': 'file'}) # кладет в список новый словарь

            print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n') # выводит в консоль обход директории


        json.dump(json_data, f_json, indent=2) # запись в файл json

        writer = csv.DictWriter(f_csv, fieldnames=fieldnames) # создаем объект csv.DictWriter
        writer.writeheader()                                  # записываем шапку таблицы в файл csv
        writer.writerows(rows)                                # записываем в таблицу списки построчно в файл csv
   
        pickle.dump(json_data, f_pickle)   # запись в файл pickle



direct_info(('Seminar_7_Home7'))
'''



import os
import csv
import json
import pickle


def structure_of_directory(dir):
    dict = {}
    os.chdir(dir)

    for _, dir_name, file_name in os.walk(os.getcwd()):
        for file in file_name:
            file_size = os.path.getsize(file) # directory + '/' + file
            dict[file] = [file, file_size]

        for i, j in dict.items():
            print(i, j)
        print()

        print(f'{dir_name = }')
        print()

        qwe = []
        for directory in dir_name:
            qwe.append(os.getcwd().split('\\')[-1] + '\\' + directory)


        print(f'{qwe = }')

        for directory in qwe:

            print(directory)
            print()

            size = 0
            for file in os.listdir(directory.split('\\')[-1]):
                if os.path.isfile(file):
                    file_size = os.path.getsize(file)
                    dict[file] = [file, file_size]
                    size += file_size
                if os.path.isdir(file):
                    dict[file] = [directory, 'f', file_size]
            dict[directory] = [os.getcwd().split('\\')[-1], 'd', size]

            for i, j in dict.items():
                print(i, j)
            print()
            
    with open('test.json', 'w', encoding='UTF-8') as f1:
        json.dump(dict, f1, indent=2, ensure_ascii=False)

'''
def json_to_csv(name):
    new_name = name.split('.')[0]
    csv_file_name = new_name + '.csv'
    with open(name, encoding='UTF-8') as f1, \
            open(csv_file_name, 'w', newline='', encoding='UTF-8') as f2:
        data = json.load(f1)
        rows = []
        for name, value in data.items():
            directory, type_f, size_f = value
            rows.append({'directory': directory, 'type': type_f, 'size_f': int(size_f), 'name': name})
        csv_write = csv.DictWriter(f2, fieldnames=['directory', 'type', 'size_f', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


def json_to_pickle(name):
    new_name = name.split('.')[0]
    pickle_file_name = new_name + '.pickle'
    # print(pickle_file_name)
    with open(name, 'r', encoding='UTF-8') as f1:
        with open(pickle_file_name, 'wb') as f2:
            data = json.load(f1)
            pickle.dump(data, f2)
'''

structure_of_directory(r'C:\Users\Tarona\Desktop\Zadachi_Python\Seminar_7_Home7')
#json_to_csv('test.json')
#json_to_pickle('test.json')





'''
import csv
import json
import os
import pickle
from pathlib import Path

PATH = Path(f'/home/ilya/Unity/Hub/Editor/2021.3.17f1/Editor/BugReporter/')


def scan_directory_and_write_info(main_path, file_name='tsk'):
    if not main_path.is_dir():
        raise Exception("Указанный каталог не доступен")
    lst_objs = []
    lst_paths = [main_path]
    while lst_paths:
        path = lst_paths.pop(0)
        for obj in os.listdir(path):
            dir_obj = {'object': obj, 'parent_dir': None, 'type_obj': None, 'size': None}
            if Path(Path(path) / obj).is_dir():
                lst_paths.append(Path(Path(path) / obj))
                dir_obj['type_obj'] = 'directory'
            if dir_obj['type_obj'] is None:
                dir_obj['type_obj'] = 'file'
            dir_obj['size'] = get_size_dir(Path(Path(path) / obj))
            dir_obj['parent_dir'] = str(path).replace(str(main_path), '')
            lst_objs.append(dir_obj)
    write_to_files(lst_objs, file_name=file_name)


def get_size_dir(path):
    if path.is_file():
        return os.path.getsize(path)
    size = 0
    for root, _, files in os.walk(path):
        for file in files:
            size += os.path.getsize(Path(Path(root) / file))
    return size


def write_to_files(lst_dict, file_name='tsk'):
    with (
        open(Path(Path().cwd() / f'{file_name}.bin'), 'wb') as file_pickle,
        open(Path(Path().cwd() / f'{file_name}.json'), 'w', encoding='UTF-8') as file_json,
        open(Path(Path().cwd() / f'{file_name}.csv'), 'w', encoding='UTF-8') as file_csv,
    ):
        json.dump(lst_dict, file_json, indent=2)
        pickle.dump(lst_dict, file_pickle)
        writer = csv.DictWriter(file_csv, fieldnames=lst_dict[0].keys(), dialect='excel-tab')
        writer.writeheader()
        writer.writerows(lst_dict)


if __name__ == '__main__':
    try:
        scan_directory_and_write_info(PATH)
    except Exception as err:
        print(err)
'''