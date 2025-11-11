"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Даны две матрицы A и B, в которых количество столбцов одинаково.
Подсчитать для каждого столбца матрицы А количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
Вывести полученные значения. Затем преобразовать матрицу В путем
умножения всех элементов столбца матрицы на посчитанное для этого столбца
значение, если оно ненулевое. Вывести преобразованную матрицу в виде
матрицы.
"""

# Импорт функции проверки str == int
from is_numeric import *

while True:
    # Ввод данных
    A = []
    print('Введите матрицу A, разделяя элементы пробелами.\n'
          'Каждая строка ввода = строка матрицы.\n'
          'После окончания ввода, введите "*"')
    row = input().split()
    if is_float(row):
        row = list(map(int, row))
        A.append(row)
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
                A.append(row)
            else:
                print(f'Строка матрицы должна содержать {n} элементов, Вы ввели {len_row} элемента.')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        continue

    B = []
    print('Введите матрицу B, разделяя элементы пробелами.\n'
          'Каждая строка ввода = строка матрицы.\n'
          'После окончания ввода, введите "*"')
    while True:
        row = input().split()
        if row == ['*']:
            break
        if is_float(row):
            row = list(map(int, row))
            len_row = len(row)
            if len_row == n:
                B.append(row)
            else:
                print(f'Строка матрицы должна содержать {n} элементов, Вы ввели {len_row} элемента.')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        continue


    # Проходимся по столбцам
    A_len = len(A)
    B_len = len(B)
    for j in range(n):
        # Считаем среднее арифмитическое
        average = 0
        for i in range(B_len):
            average += B[i][j]
        average /= B_len

        # Считаем количество элементов в A > ср.ариф.
        cnt = 0
        for i in range(A_len):
            if A[i][j] > average:
                cnt += 1
        print(cnt, end=' ')

        # Если количество > 0 => умножаем все элементы столбца B на это число
        if cnt > 0:
            for i in range(B_len):
                B[i][j] *= cnt


    # Вывод матрицы В
    # Печать итогового результата
    print()
    print('Матрица В:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in B[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)