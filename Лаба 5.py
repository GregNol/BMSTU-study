"""
Титов Матвей Алексеевич ИУ7-12Б Вар 50
Построить таблицу значений заданной функции и её график
𝑧1 = 𝑎3 − 19.1𝑎2 + 27.9𝑎 + 5.58
𝑧2 = 𝑎2 − 𝑠𝑖𝑛πa
"""

# Импорт синуса и числа Пи
from math import sin, pi

# Ввод данных
while True:
    start = float(input('Введите стартовое значение: '))
    step = float(input('Введите шаг разбиения: '))
    finish = float(input('Введите конечное значение: '))
    if finish <= start:
        print('Некорректное значения старта и конца.')
        print()
        continue
    elif step <= 0:
        print('Некорректное значение шага.')
        print()
        continue

    # Массивы из значений
    x0 = []
    y1 = []
    y2 = []

    # Считаем таблицу значений
    print('-------------------------------------------------------')
    print('|        x        |        y1       |        y2       |')
    print('-------------------------------------------------------')
    l = max(len(str(start - int(start))), len(str(finish - int(finish))), len(str(step - int(step)))) - 1
    l = pow(10, l)
    for i in range(int(start * l), int(finish * l + 1), int(step * l)):
        x = i / l
        t1 = pow(x, 3) - 19.1 * pow(x, 2) + 27.9 * x + 5.58
        t2 = pow(x, 2) - sin(pi * x)
        y1.append(t1)
        y2.append(t2)
        x0.append(x)
        print(f'|{x:^17.6g}|{t1:^17.6g}|{t2:^17.6g}|')
    print('-------------------------------------------------------')
    print()

    """
    Строим график
    Ширина 100 символов
    Расстояние между значениями 20 символов
    """
    print('График для функции 𝑧1 = 𝑎3 − 19.1𝑎2 + 27.9𝑎 + 5.58')
    # Выводим шапку таблицы
    max_y = max(y1)
    max_y = max_y + abs(max_y) * 0.001
    min_y = min(y1)
    step_y = abs(max_y - min_y) / 5
    l = max(len(str(max_y - int(max_y))), len(str(min_y - int(min_y))), len(str(step_y - int(step_y)))) - 1
    l = pow(10, l)
    print(' ' * 10, end='')
    for i in range(int(min_y * l), int(max_y * l + 1), int(step_y * l)):
        print(f'{i / l:<20.6g}', end='')
    print()

    step_y /= 20
    # Выводим саму таблицу
    for i in range(len(x0)):
        print(f'{x0[i]:<9.6g}|', end='')
        row = [' ' for _ in range(100)]
        if min_y <= 0 <= max_y:
            row[abs(int(min_y // step_y))] = '|'
        row[abs(int((y1[i] - min_y) // step_y))] = '*'
        print(*row, sep='')
    print()

    # Подсчет суммы положительных значений второй функции
    s = 0
    for i in y2:
        if i > 0:
            s += i
    print(f'Сумма положительных значений функции(𝑧2 = 𝑎2 − 𝑠𝑖𝑛πa) = {s:.6g}')
    print()
    print('__________________________________________________________________________________')
    print()
