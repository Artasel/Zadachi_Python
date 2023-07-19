import random
import csv
import json
import math


def save_to_json(func):
    def wrapper(*args, **kwargs):
        with open('for_sqrt.csv', 'r', newline='', encoding='UTF-8') as f:
            for line in f.readlines():
                tmp = []
                a, b, c = line.strip().split(',')
                result = func(int(a), int(b), int(c))
                tmp.append(a)
                tmp.append(b)
                tmp.append(c)
                tmp.append(result)
                with open('for_sqrt.json', 'a', encoding='UTF-8') as f1:
                    json.dump(tmp,f1, ensure_ascii=False)


    return wrapper


def rnd_to_csv(name):
    with open(name, 'w', newline='', encoding='UTF-8') as f:
        csv_write = csv.writer(f, dialect='excel')

        for _ in range(random.randint(100, 1000)):
            rows = []
            tmp = []
            for i in range(3):
                i = random.randint(10, 100)
                tmp.append(i)
            rows.append(tmp)
            csv_write.writerows(rows)


@save_to_json
def sqrt_finder(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x1 = x2 = -b / (2 * a)
        return x1, x2
    else:
        x1 = x2 = 'Нет корней'
        return x1, x2


rnd_to_csv('for_sqrt.csv')

sqrt_finder(0, 0, 0)


