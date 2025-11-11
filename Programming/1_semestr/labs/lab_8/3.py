"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Найти столбец, имеющий Наименьшее количество отрицательных элементов
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

    # Поиск нужного столбца
    min_cnt = r + 1
    min_id = -1
    for j in range(m):
        local_cnt = 0
        for i in range(1, r):
            if matrix[i][j] < 0:
                local_cnt += 1
        if local_cnt < min_cnt:
            min_cnt = local_cnt
            min_id = j

    # Вывод результатов
    if min_id == -1:
        print('В матрице нет отрицательных элементов')
    else:
        print(f'Результат: {[matrix[i][min_id] for i in range(r)]}')