import sorter
from math import inf


def format_time(seconds):
    """Форматирует время в читаемый вид"""
    if seconds <= 0.001:
        return f"{seconds * 1000000:.6g} мкс"  # микросекунды
    elif seconds < 1:
        return f"{seconds * 1000:.6g} мс"  # миллисекунды
    else:
        return f"{seconds:.6g} с"  # секунды


def prepare_chart_data(n1, n2):
    """Подготовка значений для построения графика"""
    res = {}
    if n2 - n1 <= 20:
        n_delta = 1
    else:
        n_delta = (n2 - n1) // 20

    max_time = -1
    min_time = inf
    for n in range(n1, n2 + 1, n_delta):
        # Определяем время выполнения
        sorted = sorter.heapsort_sorted(n)
        sorted = sorted[0]

        random = sorter.heapsort_random(n)
        random = random[0]

        reverse_sorted = sorter.heapsort_reverse_sorted(n)
        reverse_sorted = reverse_sorted[0]

        # Обновляем max/min
        max_time = max(max_time, sorted, random, reverse_sorted)
        min_time = min(min_time, sorted, random, reverse_sorted)

        # Записываем в res[N] время сортировок
        res[n] = [sorted, random, reverse_sorted]

    # Передаем в результаты максимальное и минимальное время выполнения
    res['max'] = max_time
    res['min'] = min_time

    return res


def print_chart(n1, n2):
    # Подготовка данных
    data = prepare_chart_data(n1, n2)
    max_time = data['max'] * 1.001
    min_time = data['min']

    # Определяем шаг времени, для вывода оси t графика
    step_time = abs(max_time - min_time) / 5
    l = max(len(str(max_time - int(max_time))), len(str(min_time -
            int(min_time))), len(str(step_time - int(step_time)))) - 1
    l = pow(10, l)
    # Выводим ось t для графика
    print(' ' * 10, end='')
    for i in range(int(min_time * l), int(max_time * l + 1), int(step_time * l)):
        print(f'{format_time(i / l):<20}', end='')
    print()

    step_time /= 20
    # Выводим саму таблицу
    for key, value in data.items():
        if key in ['max', 'min']:
            continue
        print(f'{key:<9.6g}|', end='')
        row = [' ' for _ in range(100)]
        row[abs(int((value[0] - min_time) // step_time))
            ] = '\033[3m\033[31m*\033[0m'
        row[abs(int((value[1] - min_time) // step_time))
            ] = '\033[3m\033[32m*\033[0m'
        row[abs(int((value[2] - min_time) // step_time))
            ] = '\033[3m\033[33m*\033[0m'
        print(*row, sep='')
    print()
    print(
        'Легенда графика: \033[3m\033[31msorted\033[0m \033[3m\033[32mrandom\033[0m \033[3m\033[33mreverse_sorted\033[0m')
