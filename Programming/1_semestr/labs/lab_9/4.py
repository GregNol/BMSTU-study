"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
"""

# Импорт функции проверки str == int
from is_numeric import *
# Импорт бесконечности
from math import inf
while True:
    # Ввод данных
    D = []
    print('Введите матрицу D, разделяя элементы пробелами.\n'
          'Каждая строка ввода = строка матрицы.\n'
          'После окончания ввода, введите "*"')
    row = input().split()
    if is_float(row):
        row = list(map(int, row))
        D.append(row)
        n = len(row)
    else:
        continue
    f_exit = 0
    while True:
        row = input().split()
        if row == ['*']:
            break
        if is_float(row):
            row = list(map(int, row))
            len_row = len(row)
            if len_row == n:
                D.append(row)
            else:
                print(f'Строка матрицы должна содержать {n} элементов, Вы ввели {len_row} элемента.')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        continue

    l = input('Введите массив l, содержащий номера строк: ').split()
    if is_int(l):
        l = list(map(int, l))
    else:
        continue

    # Проверка l, что индексы в пределах матрицы D
    D_len = len(D)
    f_exit = 0
    for i in l:
        if i > D_len:
            print('Index out of range')
            f_exit = 1
            break
    if f_exit:
        continue

    # Поиск максимальных значений
    l = list(set(l))
    r = []
    for i in l:
        ind = i - 1
        local_max = -inf
        for j in range(n):
            if D[ind][j] > local_max:
                local_max = D[ind][j]
        r.append(local_max)

    # Поиск среднего арифмитического R
    average = 0
    for i in r:
        average += i
    average /= len(r)

    # Печать матрицы D
    print()
    print('Матрица D:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in D[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)

    print(f'l: {l}')
    print(f'R: {r}')
    print(f'average: {average:.6g}')