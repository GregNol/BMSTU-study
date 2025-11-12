"""
Титов Матвей ИУ7-12Б
НАзначение: Создать и проанализировать пирамидальную сортировку
"""

# Импорт функционала для работы
import sorter
from table import print_table
from is_numeric import is_int
import chart


def main():
    while True:
        # Ввод массива
        mas = input(
            'Введите массив целых чисел, разделяя элементы пробелом: ').split()
        if len(mas) == 0:
            print('Вы ввели пустой массив')
            continue
        elif is_int(mas):
            mas = list(map(int, mas))
        else:
            continue

        # Сортировка массива
        sorter.heapsort(mas)
        # Вывод отсортированного массива
        print(f'Отсортированный массив: {mas}')

        # Вввод данных
        ns = input(
            'Введите 3 натуральных числа - размерности массивов для тестирования времени сортировки: ').split()
        if len(ns) != 3:
            print(f"Вы ввели {len(ns)} чисел. Необходимо ввести 3 числа.")
            continue
        elif len(ns) == 3 and is_int(ns):
            n1, n2, n3 = map(int, ns)
            if n1 > 0 and n2 > 0 and n3 > 0:
                pass
            else:
                print('Одно или несколько чисел не натуральные')
                continue
        else:
            continue

        # Инициализация словаря с результатами работы
        result = {}
        result['n1'] = n1
        result['n2'] = n2
        result['n3'] = n3

        # Проведение тестов и запись результатов
        result['t1'], result['k1'] = sorter.heapsort_sorted(n1)
        result['t4'], result['k4'] = sorter.heapsort_random(n1)
        result['t7'], result['k7'] = sorter.heapsort_reverse_sorted(n1)

        result['t2'], result['k2'] = sorter.heapsort_sorted(n2)
        result['t5'], result['k5'] = sorter.heapsort_random(n2)
        result['t8'], result['k8'] = sorter.heapsort_reverse_sorted(n2)

        result['t3'], result['k3'] = sorter.heapsort_sorted(n3)
        result['t6'], result['k6'] = sorter.heapsort_random(n3)
        result['t9'], result['k9'] = sorter.heapsort_reverse_sorted(n3)

        # Вывод таблицы результатов
        print_table(result)

        # Ввод n1,n2
        ns = input(
            'Введите 2 числа n1,n2 для построения графика зависимости времени сортировки от размерности массива: ').split()
        if len(ns) != 2:
            print(f'Вы ввели {len(ns)} чисел, необходимо ввести 2.')
            continue
        else:
            if is_int(ns):
                n1, n2 = list(map(int, ns))
                if n1 > 0 and n2 > n1:
                    pass
                else:
                    print('Value Error')
                    continue
            else:
                continue

        # Построение графика
        chart.print_chart(n1, n2)


if __name__ == '__main__':
    main()
