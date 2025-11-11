"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю
"""
print('В качестве количества строк и количества элементов в строке матрицы принимаются только целые положительные '
      'числа, элементы матрицы могут быть отрицательными нецелыми числами. Например, -1.01 или 23.123')
# Импорт функций проверки
from is_numeric import *
# Импорт бесконечности
from math import inf

while True:
    #Ввод информации о матрице и проверка на корректность
    r = input('Введите количество строк матрицы: ')
    if is_int(r):
        r = int(r)
        if r < 0:
            print('Количество строк должно быть положительным числом')
            break
    else:
        print('Количество строк должно быть целым числом')
        break
    m = r
    # Ввод матрицы и проверка на её корректность
    print('Введите матрицу построчно, разделяя элементы пробелами')
    f_exit = 0
    matrix = []
    for i in range(r):
        row = input().split()
        if is_float(row):
            row = list(map(float, row))
            len_row = len(row)
            if len_row == m:
                matrix.append(row)
            else:
                print(f'Строка матрицы должна содержать {m} элементов, Вы ввели {len_row} элемент')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        break

    # Печать исходной матрицы
    print()
    print('Входные данные:')
    delimer = '-' * (16 * r + 1)
    print(delimer)
    for i in range(r):
        print('|', end='')
        for j in matrix[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)

    # Поиск максимума над главной диагональю
    max_n = -inf
    for i in range(r):
        for j in range(1 + i, r):
            if matrix[i][j] > max_n:
                max_n = matrix[i][j]
    # Поиск минимума под побочной диагональю
    min_n = inf
    for i in range(r):
        for j in range(r - i, r):
            if matrix[i][j] < min_n:
                min_n = matrix[i][j]

    # Вывод результатов
    print(f'Максимум над главной диагональю: {max_n:<6g}\nМинимум под побочной диагональю: {min_n:<6g}')