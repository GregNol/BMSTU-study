from math import inf
import function


def format_float(n):
    # Форматирование чисел
    if n == '-':
        return '-'
    else:
        return f'{n:.6g}'


def prepare_chart_data(a, b):
    """Подготовка значений для построения графика"""
    res = {}
    x_delta = abs(b - a) // 100

    max_y = -inf
    min_y = inf

    x = a
    while x <= b:
        y_f = function.f(x)
        y_g = function.g(x)
        max_y = max(y_f, y_g, max_y)
        min_y = min(y_f, y_g, min_y)
        res[x] = [y_f, y_g]
        x += x_delta
    # Передаем в результаты максимальное и минимальное время выполнения
    res['max'] = max_y
    res['min'] = min_y

    return res


def print_chart(a, b, zero_left, zero_right):
    # Подготовка данных
    data = prepare_chart_data(a, b)
    max_y = data['max'] * 1.001
    min_y = data['min']

    # Определяем шаг y, для вывода оси OY графика
    step_y = abs(max_y - min_y) / 5
    l = max(len(str(max_y - int(max_y))), len(str(min_y -
            int(min_y))), len(str(step_y - int(step_y)))) - 1
    l = pow(10, l)
    # Выводим ось OY для графика
    print(' ' * 10, end='')
    for i in range(int(min_y * l), int(max_y * l + 1), int(step_y * l)):
        print(f'{format_float(i / l):<20}', end='')
    print()

    step_y /= 20
    # Выводим саму таблицу
    for x, value in data.items():
        if x in ['max', 'min']:
            continue
        print(f'{x:<9.6g}|', end='')
        row = [' ' for _ in range(100)]
        f_i = abs(int((value[0] - min_y) // step_y))
        g_i = abs(int((value[1] - min_y) // step_y))
        if f_i == g_i:
            row[f_i] = '\033[3m\033[33m*\033[0m'
        else:
            row[f_i] = '\033[3m\033[31m*\033[0m'
            row[g_i] = '\033[3m\033[32m*\033[0m'
            if zero_left < x < zero_right:
                for i in range(min(f_i, g_i) + 1, max(f_i, g_i)):
                    row[i] = '\033[3m\033[34m-\033[0m'

        print(*row, sep='')
    print()
    print(
        'Легенда графика: \033[3m\033[31mf(x)\033[0m \033[3m\033[32mg(x)\033[0m \033[3m\033[33mf(x)=g(x)\033[0m \033[3m\033[34mПлощадь между графиками\033[0m')
