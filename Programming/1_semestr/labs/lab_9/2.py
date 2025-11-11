"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
вводить. Транспонирование не применять.
"""

# Импорт функции проверки str == int
from is_numeric import *

while True:
    # Ввод данных
    m = []
    print('Введите квадратную целочисленную матрицу, разделяя элементы пробелами.\n'
          'Каждая строка ввода = строка матрицы.')
    row = input().split()
    if is_int(row):
        row = list(map(int, row))
        m.append(row)
        n = len(row)
    else:
        continue
    f_exit = 0
    for i in range(n - 1):
        row = input().split()
        if is_int(row):
            row = list(map(int, row))
            len_row = len(row)
            if len_row == n:
                m.append(row)
            else:
                print(f'Строка матрицы должна содержать {n} элементов, Вы ввели {len_row} элемента.')
                f_exit = 1
                break
        else:
            f_exit = 1
            break
    if f_exit:
        continue

    # Печать исходной матрицы
    print()
    print('Входные данные:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in m[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)


    # Поворот матрицы на 90 по часовой стрелке
    for i in range(n // 2):
        for j in range(n - i * 2 - 1):
            m[i][i + j], m[i + j][-i - 1], m[-i - 1][-i - 1 - j], m[-i - 1 - j][i] = m[-i - 1 - j][i], m[i][i + j], m[i + j][-i - 1], m[-i - 1][-i - 1 - j]

    # Печать промежуточного результата
    print()
    print('Промежуточный результат:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in m[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)

    # Поворот матрицы на 90 против часовой стрелки
    for i in range(n // 2):
        for j in range(n - i * 2 - 1):
            m[i][i + j], m[i + j][-i - 1], m[-i - 1][-i - 1 - j], m[-i - 1 - j][i] = m[i + j][-i - 1], m[-i - 1][-i - 1 - j], m[-i - 1 - j][i], m[i][i + j]

    # Печать итогового результата
    print()
    print('Итоговый результат:')
    delimer = '-' * (16 * n + 1)
    print(delimer)
    for i in range(n):
        print('|', end='')
        for j in m[i]:
            print(f'{j:^15.6g}|', end='')
        print()
        print(delimer)