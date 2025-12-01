"""
Титов Матвей ИУ7-12Б
Назначение: продемонстрировать работу метода правых прямоугольников и метода парабол
"""

# Импорт проверки типа введенных данных
from is_numeric import *
import integrals
import tables
import function
import chart
global_eps = 1e-8


def main():
    print('Интегрируемая функция: y=-cos(x) * (x ** 2) + 2 * sin(x) * x + 10')

    # Ввод границ отрезка
    while True:
        ns = input(
            'Введите два числа a и b через пробел, для которых на отрезке [a,b] будет посчитан интеграл: ').split()
        if len(ns) == 2:
            if is_float(ns):
                start, end = map(float, ns)
                if end > start:
                    break
                else:
                    print(ValueError('b должно быть больше a'))
            else:
                continue
        else:
            print(ValueError(
                f'Вы ввели {len(ns)} элементов, необходимо ввести 2 элемента.'))

    # Ввод количества разбиений
    while True:
        ns = input(
            'Введите два натуральных четных числа n1 и n2 через пробел - количество разбиений для подсчета интеграла: ').split()
        if len(ns) == 2:
            if is_int(ns):
                n1, n2 = map(int, ns)
                if n1 > 0 and n2 > 0:
                    break
                else:
                    print(ValueError('Вы ввели ненатуральные числа'))
            else:
                continue
        else:
            print(ValueError(
                f'Вы ввели {len(ns)} элементов, необходимо ввести 2 элемента.'))

    # Считаем интегралы
    I = integrals.integral(start, end)
    print(f'Значение интеграла: {I:.6g}')
    I1 = integrals.right_rect(function.y, start, end, n1)
    I1_absolut = abs(I1 - I)
    I1_relative = abs(I1_absolut / I) * 100

    I2 = integrals.right_rect(function.y, start, end, n2)
    I2_absolut = abs(I2 - I)
    I2_relative = abs(I2_absolut / I) * 100

    if n1 % 2 == 0:
        I3 = integrals.simpson(function.y, start, end, n1)
        I3_absolut = abs(I3 - I)
        I3_relative = abs(I3_absolut / I) * 100
    else:
        I3 = 0
        I3_absolut = 0
        I3_relative = 0

    if n2 % 2 == 0:
        I4 = integrals.simpson(function.y, start, end, n2)
        I4_absolut = abs(I4 - I)
        I4_relative = abs(I4_absolut / I) * 100
    else:
        I4 = 0
        I4_absolut = 0
        I4_relative = 0

    # Выводим таблицу результатов
    tables.table_results(I1, I1_absolut, I1_relative, I2, I2_absolut, I2_relative,
                         I3, I3_absolut, I3_relative, I4, I4_absolut, I4_relative, n1, n2)

    # Ищем худший результат и считаем значение интеграла с заданной точностью
    max_absolut = max(I1_absolut, I2_absolut, I3_absolut, I4_absolut)
    if (I1_absolut - global_eps < max_absolut < I1_absolut + global_eps) or max_absolut == I2_absolut:
        print('Метод правого квадрата показал худшее отклонение')
        # Ввод точности
        while True:
            eps = input(
                'Введите число для поиска значения интеграла с заданной точностью: ')
            if is_float(eps):
                eps = float(eps)
                if eps > 0:
                    break
                else:
                    print('Точность должна быть положительным числом')
        # Расчет интеграла
        n = 1
        i_local_1 = integrals.right_rect(function.y, start, end, n)
        i_local_2 = integrals.right_rect(function.y, start, end, 2 * n)
        while abs(i_local_1 - i_local_2) >= eps and abs(i_local_1 - I) > eps:
            n *= 2
            i_local_1 = i_local_2
            i_local_2 = integrals.right_rect(function.y, start, end, 2 * n)
        print(
            f'Интеграл вычислен с заданной точностью при n = {n:.6g}. Значение интеграла = {integrals.right_rect(function.y, start, end, n):.6g}')
    else:
        print('Метод парабол показал худшее отклонение')
        # Ввод точности
        while True:
            eps = input(
                'Введите число для поиска значения интеграла с заданной точностью: ')
            if is_float(eps):
                eps = float(eps)
                if eps > 0:
                    break
                else:
                    print('Точность должна быть положительным числом')
        # Расчет интеграла
        n = 2
        i_local_1 = integrals.simpson(function.y, start, end, n)
        i_local_2 = integrals.simpson(function.y, start, end, 2 * n)
        while abs(i_local_1 - i_local_2) >= eps and abs(i_local_1 - I) > eps:
            n *= 2
            i_local_1 = i_local_2
            i_local_2 = integrals.simpson(function.y, start, end, 2 * n)
        print(
            f'Интеграл вычислен с заданной точностью при n = {n:.6g}. Значение интеграла = {integrals.simpson(function.y, start, end, n):.6g}')
        print()

    # Часть 2
    # Ввод границ отрезка
    while True:
        ns = input(
            'Введите два числа a и b через пробел, для которых на отрезке [a,b] будет найдена площадь между двумя графиками: ').split()
        if len(ns) == 2:
            if is_float(ns):
                start, end = map(float, ns)
                if end > start:
                    break
                else:
                    print(ValueError('b должно быть больше a'))
            else:
                continue
        else:
            print(ValueError(
                f'Вы ввели {len(ns)} элементов, необходимо ввести 2 элемента.'))

    # Ввод точности
    while True:
        eps = input(
            'Введите точность для поиска площади образованной графиками f(x) и g(x) замкнутой фигуры: ')
        if is_float(eps):
            eps = float(eps)
            if eps > 0:
                break
            else:
                print('Точность должна быть положительным числом')

    # Получение нулей на отрезке [start, end]
    zeros = function.get_zero(
        lambda x: function.f(x) - function.g(x), start, end)
    cnt_zero = len(zeros)
    if cnt_zero == 0:
        print('Функции не пересекаются')
    elif cnt_zero == 1:
        print('Функции имеют 1 пересечение на заданном промежутке, посчитать площадь невозможно')
    else:
        n = 10
        def local_func(x): return abs(function.f(x) - function.g(x))
        i_local_1 = integrals.simpson(local_func, start, end, n)
        i_local_2 = integrals.simpson(local_func, start, end, 2 * n)
        while abs(i_local_1 - i_local_2) >= eps:
            n *= 2
            i_local_1 = i_local_2
            i_local_2 = integrals.simpson(local_func, start, end, 2 * n)
        i = integrals.simpson(lambda x: abs(function.f(
            x) - function.g(x)), zeros[0], zeros[-1], n)
        print(
            f'Количество пересечений функций = {cnt_zero:.6g}; Площадь между графиками = {i:.6g}')
        print(f'Нули функции: {[f"{z:.6g}" for z in zeros]}')

        # Построение графика
        chart.print_chart(start, end, zeros[0], zeros[-1])


if __name__ == '__main__':
    while True:
        main()
