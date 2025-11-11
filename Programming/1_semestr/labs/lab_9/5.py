"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
В. Вывести все матрицы в виде матриц
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
    print(f'Введите матрицу B из {n} строк разделяя элементы пробелами.\n'
          f'Каждая строка ввода = строка матрицы.')
    row = input().split()
    if is_float(row):
        row = list(map(int, row))
        B.append(row)
        m = len(row)
    else:
        continue
    f_exit = 0
    for _ in range(n - 1):
        row = input().split()
        if row == ['*']:
            break
        if is_float(row):
            row = list(map(int, row))
            len_row = len(row)
            if len_row == m:
                B.append(row)
            else:
                print(f'Строка матрицы должна содержать {m} элементов, Вы ввели {len_row} элемента.')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        continue


    # Печать матрицы A
    A_len = len(A)
    print()
    print('Матрица A:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(A_len):
        print('|', end='')
        for j in A[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)

    # Печать матрицы B
    print()
    print('Матрица B:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in B[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)


    # Создание матрицы С
    C = []
    for i in range(A_len):
        row = []
        for j in range(m):
            el = 0
            for k in range(n):
                el += A[i][k] * B[k][j]
            row.append(el)
        C.append(row)


    # Печать матрицы C
    print()
    print('Матрица C:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(A_len):
        print('|', end='')
        for j in C[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)