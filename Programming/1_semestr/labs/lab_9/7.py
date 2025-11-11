"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону
"""


# Импорт функции проверки str == int
from is_numeric import *

while True:
    # Ввод матрицы
    matrix_size = input('Введите размеры матрицы в формате X, Y, Z, разделяя параметры через пробел: ').split()
    len_input = len(matrix_size)
    if len_input == 3:
        if is_int(matrix_size):
            matrix_size = list(map(int, matrix_size))
            if matrix_size[0] > 0 and matrix_size[1] > 0 and matrix_size[2] > 0:
                matrix_x = matrix_size[0]
                matrix_y = matrix_size[1]
                matrix_z = matrix_size[2]
            else:
                print('Все параметры должны быть натуральными числами.')
                continue
        else:
            continue
    else:
        print(f'Вам необходимо ввести 3 элемента, вы ввели {len_input} элементов')
        continue

    # Поиск максимальной размерности
    matrix_max = matrix_x
    if matrix_max < matrix_y:
        matrix_max = matrix_y
    if matrix_max < matrix_z:
        matrix_max = matrix_z

    # Проверка на единственность наибольшего среза
    if int(matrix_x == matrix_max) + int(matrix_y == matrix_max) + int(matrix_z == matrix_max) > 1:
        print('Максимальная размерность определяется не однозначно.')
        continue

    # Ввод матрицы
    matrix = [] # z, x, y
    print('Введите матрицу по слоям. i-ая строка = координата X, j-ый столбец = координата Y')
    f_exit = 0
    for z in range(matrix_z):
        print(f'z = {z}')
        matrix_slice = []
        for x in range(matrix_x):
            row = input().split()
            len_row = len(row)
            if len_row == matrix_y:
                if is_float(row):
                    row = list(map(float, row))
                    matrix_slice.append(row)
                else:
                    f_exit = 1
                    break
            else:
                print(f'Вам необходимо ввести {matrix_y} элементов, вы ввели {len_row} элементов')
                f_exit = 1
                break
        if f_exit:
            break
        matrix.append(matrix_slice)
    if f_exit:
        continue


    # Вывод среза
    if matrix_max == matrix_x:
        x = matrix_x // 2
        print(f'Матрица имеет максимальную размерность по X, срез будет выведен по X = {x:.6g}')
        print('Ось Z направлена вниз, Y вправо')
        # Печать матрицы
        matrix_len = len(matrix)
        print()
        print('Результат работы:')
        delimer = '-' * (6 * matrix_y + 1)
        print(delimer)
        for i in range(matrix_z):
            print('|', end='')
            for j in matrix[i][x]:
                print(f'{j:^5}|', end='')
            print()
            print(delimer)
    if matrix_max == matrix_y:
        y = matrix_y // 2
        print(f'Матрица имеет максимальную размерность по Y, срез будет выведен по Y = {x:.6g}')
        print('Ось Z направлена вниз, X вправо')
        # Печать матрицы
        matrix_len = len(matrix)
        print()
        print('Результат работы:')
        delimer = '-' * (6 * matrix_x + 1)
        print(delimer)
        for i in range(matrix_z):
            print('|', end='')
            for j in matrix[i]:
                print(f'{j[y]:^5}|', end='')
            print()
            print(delimer)
    if matrix_max == matrix_z:
        z = matrix_z // 2
        print(f'Матрица имеет максимальную размерность по Z, срез будет выведен по Z = {z:.6g}')
        print('Ось Х направлена вниз, Y вправо')
        # Печать матрицы
        matrix_len = len(matrix)
        print()
        print('Результат работы:')
        delimer = '-' * (6 * matrix_y + 1)
        print(delimer)
        for i in range(matrix_x):
            print('|', end='')
            for j in matrix[z][i]:
                print(f'{j:^5}|', end='')
            print()
            print(delimer)