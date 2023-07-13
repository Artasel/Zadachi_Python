'''
Решить задачи, которые не успели решить на семинаре.
Напишите функцию группового переименования файлов. Она должна:
         5-принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.
    1-принимать параметр количество цифр в порядковом номере.
     2-принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
      3-принимать параметр расширение конечного файла.
       4-принимать диапазон сохраняемого оригинального имени. 
Например:
для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами.
'''

import os

# os.chdir('C:/Users/Tarona/Desktop/Zadachi_Python/Seminar_7, _Home7')

def rename_file_func(number_digits: int, source_extension: str, end_extension: str, range_original_name: list[int, int], desired_name = ''):
    number = 0

    def number_digits_file(num_dig, num):
        str_num = str(num)
        res_num = '0' * (num_dig - len(str_num)) + str_num
        return res_num

    for _, _, file_name in os.walk(os.getcwd()):
        for i in file_name:
            result_name = ''
            if i.split('.')[1] == source_extension:  
                min, max = range_original_name
                if len(i.split('.')[0]) < max:
                    max = len(i.split('.')[0])

                if len(i.split('.')[0]) <= min:
                    result_name += i.split('.')[0]
                else:
                    result_name += i.split('.')[0][min: max]
                
                number += 1
                res_num = number_digits_file(number_digits, number)

                result_name += '_' + desired_name + res_num
   
                os.rename(i, result_name + '.' + end_extension)  
    
    for _, _, file_name in os.walk(os.getcwd()):
        print(f'{file_name = }')



if __name__ == '__main__':
    range_name = [1, 8]
    rename_file_func(6, 'json', 'txt', range_name)
