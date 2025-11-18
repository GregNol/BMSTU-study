"""
Титов Матвей ИУ7-12Б
Назначение: продемонстрировать работу метода правых прямоугольников и метода парабол
"""

# Импорт проверки типа введенных данных
from is_numeric import *
import integrals
import tables
import function


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
            'Введите два натуральных четных числа n1 и n2 чеоез пробел - количество разбиений для подсчета интеграла: ').split()
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
    I1 = integrals.right_rect(start, end, n1)
    I1_absolut = abs(I1 - I)
    I1_relative = abs(I1_absolut / I)

    I2 = integrals.right_rect(start, end, n2)
    I2_absolut = abs(I2 - I)
    I2_relative = abs(I2_absolut / I)

    if n1 % 2 == 0:
        I3 = integrals.simpson(start, end, n1)
        I3_absolut = abs(I3 - I)
        I3_relative = abs(I3_absolut / I)
    else:
        I3 = 0
        I3_absolut = 0
        I3_relative = 0

    if n2 % 2 == 0:
        I4 = integrals.simpson(start, end, n2)
        I4_absolut = abs(I4 - I)
        I4_relative = abs(I4_absolut / I)
    else:
        I4 = 0
        I4_absolut = 0
        I4_relative = 0

    # Выводим таблицу результатов
    tables.table_results(I1, I1_absolut, I1_relative, I2, I2_absolut, I2_relative,
                         I3, I3_absolut, I3_relative, I4, I4_absolut, I4_relative, n1, n2)

    # Ищем худший результат и считаем значение интеграла с заданной точностью
    max_absolut = max(I1_absolut, I2_absolut, I3_absolut, I4_absolut)
    if max_absolut == I1_absolut or max_absolut == I2_absolut:
        print('Метод правого квадрата показал худшее отклонение')
        while True:
            eps = input(
                'Введите число для поиска значения интеграла с заданной точностью: ')
            if is_float(eps):
                eps = float(eps)
                break

        n = min(n1, n2)
        while abs(integrals.right_rect(start, end, n) - integrals.right_rect(start, end, 2 * n)) >= eps:
            n *= 2

        print(
            f'Интеграл вычислен с заданной точностью при n = {n:.6g}. Значение интеграла = {integrals.right_rect(start, end, n):.6g}')
    else:
        print('Метод парабол показал худшее отклонение')
        while True:
            eps = input(
                'Введите число для поиска значения интеграла с заданной точностью: ')
            if is_float(eps):
                eps = float(eps)
                break

        n = min(n1, n2)
        if n % 2 == 1:
            n = max(n1, n2)
        while abs(integrals.simpson(start, end, n) - integrals.simpson(start, end, 2 * n)) >= eps:
            n *= 2

        print(
            f'Интеграл вычислен с заданной точностью при n = {n:.6g}. Значение интеграла = {integrals.simpson(start, end, n):.6g}')


if __name__ == '__main__':
    main()
