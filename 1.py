'''
num = int(input('Введите год!!! '))

if(num < 1582):
    res = 'Нет календаря'
elif(num % 4 != 0 or num % 100 == 0 and num % 400 != 0):
    res = 'Невысокосный'
else:
    res = 'Высокосный'

print(res)
'''


'''
zv = '*'
prob = ' '

hite = int(input('Введите высоту'))
shir = hite - 1

col_zv = 1

while hite > 0:
    for i in range(shir):
        print(prob, end="")

    for i in range(col_zv):
        print(zv, end="")

    shir -= 1
    col_zv += 2
    hite -= 1
    print()
'''


'''
rows = int(input('Введите количество рядов у елки: '))
symbol = 1
while rows > 0:
    print(' ' * rows, '*' * symbol)
    rows -= 1
    symbol += 2
'''

'''
for i in range(2, 10):
    for j in range(2, 6):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()


print()

for i in range(2, 10):
    for j in range(6, 10):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()
'''

'''
i = 0
while not i in range(1, 1000):
    try:
        i = int(input("Введите число: "))

    except ValueError:
        print("Неверное число")

if i / 10 < 1:
    print(i ** 2)
elif i / 100 < 1:
    print(i // 10 * (i % 10))
elif i / 1000 < 1:
    print(int(f"{i % 10}{i // 10 % 10}{i // 100}"))
'''
