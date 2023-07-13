'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните 
в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами разных форматов.
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
