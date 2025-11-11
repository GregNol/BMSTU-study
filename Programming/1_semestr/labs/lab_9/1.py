"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Даны два одномерных целочисленных массива A и B.
Сформировать матрицу M, такую что 𝑚𝑖𝑗 = 𝑎𝑖 * 𝑏𝑗
Определить количество полных квадратов в каждой строке матрицы. Записать
значения в массив S. Напечатать матрицу M в виде матрицы
и рядом столбец S.
"""

# Импорт функции проверки str == int
from is_numeric import *

while True:
    # Ввод данных
    a = input('Введите целочисленный массив a, разделяя элементы пробелами: ').split()
    if is_int(a):
        a = list(map(int, a))
    else:
        continue
    
    b = input('Введите целочисленный массив b, разделяя элементы пробелами: ').split()
    if is_int(b):
        b = list(map(int, b))
    else:
        continue
    
    # Создание матрицы M и массива S
    a_len = len(a)
    b_len = len(b)

    m = [[0 for __ in range(b_len)] for _ in range(a_len)]
    s = [0 for _ in range(a_len)]
    for i in range(a_len):
        for j in range(b_len):
            m[i][j] = a[i] * b[j]
            if m[i][j] ** 0.5 == int(m[i][j] ** 0.5):
                s[i] += 1


    # Вывод результатов
    delimer = '-' * (1 + 16 * (b_len + 1))
    print()
    print('Результат работы: ')
    print(delimer)
    print(f'|{"m":^{b_len * 16 - 1}}|{"s":^15}|')
    print(delimer)
    for i in range(a_len):
        print('|', end='')
        for j in range(b_len):
            print(f'{m[i][j]:^15.6g}|', end='')
        print(f'{s[i]:^15.6g}|')
        print(delimer)