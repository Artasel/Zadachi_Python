'''
Напишите функцию, которая заполняет файл 
(добавляет в конец) случайными парами чисел. 
Первое число int, второе - float разделены вертикальной чертой. 
Минимальное число - -1000, максимальное - +1000. 
Количество строк и имя файла передаются как аргументы функции.
'''
import os
import random
import shutil




def fill_file(name, count_lines):
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(count_lines):
            print(f'{random.randint(-1000, 1000)} | {random.uniform(-1000, 1000)}', file=f)

if __name__ == '__main__':
    fill_file('1.txt', 100)


'''
Напишите функцию, которая генерирует псевдоимена. 
Имя должно начинаться с заглавной буквы, 
состоять из 4-7 букв, среди которых 
обязательно должны быть гласные. 
Полученные имена сохраните в файл.
'''

def fill_file_2(name, count_lines):
    with open(name, 'a', encoding='utf-8') as f:
        for j in range(count_lines):
            length = random.randint(4, 8)
            check = True
            while check:
                password = ''
                for _ in range(length):
                    tmp = chr(random.randint(97, 122))
                    password = password + tmp
                    if tmp in ['a', 'o', 'u', 'i', 'e']:
                        check = False

            print(password.capitalize(), file=f)

if __name__ == '__main__':
    fill_file_2('h2.txt', 10)






'''
Напишите функцию, которая открывает на чтение созданные 
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните 
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
При достижении конца более короткого файла, 
возвращайтесь в его начало.
'''

def func(name1, name2, name3):
    with open(name1, encoding='utf-8') as f1, \
    open(name2, encoding='utf-8') as f2, \
    open(name3, 'a', encoding='utf-8') as f3:
        text1 = f1.readlines()
        text2 = f2.readlines()
        max_len = max(len(text1),  len(text2))
        i1 = 0
        i2 = 0
        for _ in range(max_len):
            a, b = text1[i1].split('|')
            a = int(a)
            b = float(b)
            c = a * b
            name_tmp = text2[i2]
            if c < 0:
                print(f'{name_tmp.strip().lower()} {abs(c)}', file=f3)
            else:
                print(f'{name_tmp.strip().upper()} {round(c)}', file=f3)
            i1 += 1
            i2 += 1
            if i1 >= len(text1):
                i1 = 0
            if i2 >= len(text2):
                i2 = 0

if __name__ == '__main__':
    func('h1.txt', 'h2.txt', 'h3.txt')




'''
Создайте функцию, которая создаёт файлы с указанным расширением. 
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''

def file_extension(extension, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, num_files=42):
    for i in range(num_files):
        name = ''
        for _ in range(random.randint(min_length, max_length)):
            tmp = chr(random.randint(97, 122))
            name = name + tmp
        with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
            for _ in range(random.randint(min_bytes, max_bytes)):
                print(chr(random.randint(97, 122)), file=f, end='')


if __name__ == '__main__':
    file_extension('jpg',num_files=1)






'''
Доработаем предыдущую задачу. 
Создайте новую функцию которая генерирует файлы с разными расширениями. 
Расширения и количество файлов функция принимает в качестве параметров. 
Количество переданных расширений может быть любым. 
Количество файлов для каждого расширения различно. 
Внутри используйте вызов функции из прошлой задачи.
'''


def file_extensions(extensions, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    for extension in extensions:
        for _ in range (extensions[extension]):
            name = ''
            for _ in range(random.randint(min_length, max_length)):
                tmp = chr(random.randint(97, 122))
                name = name + tmp
            with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
                for k in range(random.randint(min_bytes, max_bytes)):
                    print(chr(random.randint(97, 122)), file=f, end='')

if __name__ == '__main__':
    file_extensions({'jpg':1, 'pdf':2, 'txt':3})


'''
Дорабатываем функции из предыдущих задач. 
Генерируйте файлы в указанную директорию — отдельный параметр функции. 
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''


def file_extensions_folder(folder, extensions, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for extension in extensions:
        for _ in range(extensions[extension]):
            check = True
            while check:
                name = ''
                for _ in range(random.randint(min_length, max_length)):
                    tmp = chr(random.randint(97, 122))
                    name = name + tmp
                if not os.path.isfile(f'{name}.{extension}'):
                    check = False

            with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
                for k in range(random.randint(min_bytes, max_bytes)):
                    print(chr(random.randint(97, 122)), file=f, end='')

if __name__ == '__main__':
    file_extensions_folder('tmp1',{'jpg': 2, 'pdf': 1})




'''
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
Каждая группа включает файлы с несколькими расширениями. 
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

def func_sort(d, folder):
    for _, _, files in os.walk(folder):
        for file in files:
            ext = file.split('.')[-1]
            for item in d:
                if ext in d[item]:
                    if not os.path.isdir(item):
                        os.mkdir(item)
                    shutil.move(f'{folder}/{file}',item)

if __name__ == '__main__':
    func_sort({'video': ['avi', 'mov'],
           'pictures': ['jpg', 'png'], }, 'tmp1')


