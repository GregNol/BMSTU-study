"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Найти столбец, имеющий Наименьшее количество отрицательных элементов
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
    min_sum = inf
    min_id = -1
    max_sum = -inf
    max_id = -1
    for j in range(m):
        local_sum = 0
        for i in range(1, r):
            local_sum += matrix[i][j]
        if local_sum > max_sum:
            max_sum = local_sum
            max_id = j
        if local_sum < min_sum:
            min_sum = local_sum
            min_id = j

    # Вывод результатов
    if (min_id == -1) or (max_id == -1):
        print('Error')
    elif min_id == max_id:
        print('Все столбцы имеют одинаковую сумму элементов')
    else:
        # Перестановка столбцов
        for i in range(r):
            matrix[i][min_id], matrix[i][max_id]= matrix[i][max_id], matrix[i][min_id]
        # Печать результата
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