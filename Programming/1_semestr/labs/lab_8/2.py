"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
"""
print('В качестве количества строк и количества элементов в строке матрицы принимаются только целые положительные '
      'числа, элементы матрицы могут быть отрицательными нецелыми числами. Например, -1.01 или 23.123')
# Импорт функций проверки
from is_numeric import *

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
    m = input('Введите количество элементов в каждой строке: ')
    if is_int(m):
        m = int(m)
        if m < 0:
            print('Количество элементов должно быть положительным числом')
            break
    else:
        print('Количество элементов должно быть целым числом')
        break

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

    # Поиск нужной строки
    min_cnt_otr = m + 1
    min_id_otr = -1
    max_cnt_otr = 0
    max_id_otr = -1

    for i in range(r):
        local_cnt = 0
        for j in matrix[i]:
            if j < 0:
                local_cnt += 1
        if local_cnt > max_cnt_otr:
            max_cnt_otr = local_cnt
            max_id_otr = i
        if 0 < local_cnt < min_cnt_otr:
            min_cnt_otr = local_cnt
            min_id_otr = i

    # Перестановка строк
    if max_cnt_otr == 0:
        print('Матрица не содержит отрицательных элементов')
    else:
        matrix[min_id_otr], matrix[max_id_otr] = matrix[max_id_otr], matrix[min_id_otr]


    # Печать исходной матрицы
    print()
    print('Результат:')
    delimer = '-' * (16 * r + 1)
    print(delimer)
    for i in range(r):
        print('|', end='')
        for j in matrix[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)