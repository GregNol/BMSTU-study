"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Программа, которая по введенным
целочисленным координатам трех точек на плоскости
вычисляет длины сторон образованного треугольника и
длину высоты, проведенной из наименьшего угла.
Определить, является ли треугольник остроугольным.
Далее вводятся координаты точки. Определить,
находится ли точка внутри треугольника. Если да, то
найти расстояние от точки до ближайшей стороны
треугольника.
"""
# Импорт функции квадратного корня
from math import sqrt
eps = pow(10, -6) # погрешность
while True:
    # Ввод данных

    # Координаты первой точки
    xa = int(input("Введите координату Х точки A: "))
    ya = int(input("Введите координату Y точки A: "))
    print()
    # Координаты второй точки
    xb = int(input("Введите координату Х точки B: "))
    yb = int(input("Введите координату Y точки B: "))
    print()
    # Координаты третей точки
    xc = int(input("Введите координату Х точки C: "))
    yc = int(input("Введите координату Y точки C: "))
    print()
    # Проверка на уникальность точек
    if (xa == xb and ya == yb) or (xb == xc and yb == yc) or (xa == xc and ya == yc):
        print('Среди введенных координат точек 2 или более точки совпадают')
        continue
    # Проверка на перпендикулярность оси OX
    ab_is_ok = 1
    bc_is_ok = 1
    ac_is_ok = 1
    if xa - xb == 0:
        ab_is_ok = 0
    if xb - xc == 0:
        bc_is_ok = 0
    if xa - xc == 0:
        ac_is_ok = 0
    # Посчитаем уравнения прямой для каждого отрезка
    # AB
    k_ab = - (yb - ya) / (xb - xa) if ab_is_ok else 0
    b_ab = - ya - k_ab * xa if ab_is_ok else 0
    # BC
    k_bc = - (yb - yc) / (xb - xc) if bc_is_ok else 0
    b_bc = - yc - k_bc * xc if bc_is_ok else 0
    # AC
    k_ac = - (yc - ya) / (xc - xa) if ac_is_ok else 0
    b_ac = - ya - k_ac * xa if ac_is_ok else 0

    # Если все три точки лежат на одной прямой, то такого треугольника не существует
    if k_ab == k_bc == k_ac and b_bc == b_ac == b_ab:
        print('Все точки лежат на одной прямой, такого треугольника не существует')
        print()
        continue

    # Вычисляем длины сторон по Теореме Пифагора
    ab_len = sqrt(pow(xb - xa, 2) + pow(yb - ya, 2))
    bc_len = sqrt(pow(xb - xc, 2) + pow(yb - yc, 2))
    ac_len = sqrt(pow(xc - xa, 2) + pow(yc - ya, 2))

    print(f'|AB| = {ab_len:.6g}')
    print(f'|BC| = {bc_len:.6g}')
    print(f'|AC| = {ac_len:.6g}')

    """
    Против меньшей стороны лежит меньший угол
    Используя уравнение прямой, можно посчитать расстояние от наименьшей стороны до
    вершины с наименьшим углом.
    """

    # Поиск минимальной стороны
    min_abc = min(ac_len, ab_len, bc_len)
    # Поиск высоты к каждой стороне
    height_ab = abs(k_ab * xc + yc + b_ab) / sqrt(pow(k_ab, 2) + 1) if ab_is_ok else abs(xc - xa)
    height_bc = abs(k_bc * xa + ya + b_bc) / sqrt(pow(k_bc, 2) + 1) if bc_is_ok else abs(xa - xb)
    height_ac = abs(k_ac * xb + yb + b_ac) / sqrt(pow(k_ac, 2) + 1) if ac_is_ok else abs(xb - xa)
    if min_abc == ab_len:
        print(f'Высота из наименьшего угла C = {height_ab:.6g}')
    elif min_abc == bc_len:
        print(f'Высота из наименьшего угла A = {height_bc:.6g}')
    elif min_abc == ac_len:
        print(f'Высота из наименьшего угла B = {height_ac:.6g}')

    # Если квадрат большей стороны < суммы квадратов двух других сторон, то треугольник остроугольный
    max_len = max(ab_len, ac_len, bc_len)
    if ab_len ** 2 + ac_len ** 2 + bc_len ** 2 - max_len ** 2 > max_len ** 2:
        print('Треугольник ABC - остроугольный')
    else:
        print('Треугольник ABC - не остроугольный')
    print()

    # Ввод точки D
    xd = int(input("Введите координату Х точки D: "))
    yd = int(input("Введите координату Y точки D: "))
    print()
    """
    Если площадь треугольника меньше, чем площадь треугольников, образованных тремя сторонами и точкой D,
    то D не принадлежит треугольнику ABC
    """
    # Вычисление расстояния от точки до каждой прямой
    h_ab = abs(k_ab * xd + yd + b_ab) / sqrt(pow(k_ab, 2) + 1) if ab_is_ok else abs(xd - xa)
    h_bc = abs(k_bc * xd + yd + b_bc) / sqrt(pow(k_bc, 2) + 1) if bc_is_ok else abs(xd - xb)
    h_ac = abs(k_ac * xd + yd + b_ac) / sqrt(pow(k_ac, 2) + 1) if ac_is_ok else abs(xd - xc)
    print(h_ab * ab_len + h_ac * ac_len + h_bc * bc_len)
    print((height_ab * ab_len) + 2 * eps)
    print(h_ac, h_bc, h_ab)
    if (h_ab * ab_len + h_ac * ac_len + h_bc * bc_len) <= (height_ab * ab_len) + 2 * eps:
        print('Точка D лежит внутри треугольника')
        min_h = min(h_ab, h_bc, h_ac)
        if min_h == h_ab:
            print(f'Расстояние от точки D минимально до стороны AB = {min_h:.6g}')
        elif min_h == h_bc:
            print(f'Расстояние от точки D минимально до стороны BC = {min_h:.6g}')
        elif min_h == h_ac:
            print(f'Расстояние от точки D минимально до стороны AC = {min_h:.6g}')
    else:
        print('Точка D лежит вне треугольника')
    print()