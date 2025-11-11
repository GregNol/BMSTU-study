def format_time(seconds):
    """Форматирует время в читаемый вид"""
    if seconds <= 0.001:
        return f"{seconds * 1000000:.6g} мкс"  # микросекунды
    elif seconds < 1:
        return f"{seconds * 1000:.6g} мс"  # миллисекунды
    else:
        return f"{seconds:.6g} с"  # секунды


def print_table(args: dict):
    # Вывод таблицы для трех тестов
    delimer = '-' * (14 + 33 * 3)
    print(delimer)
    print(f"|{' ' * 12}|{'N1':^33}|{'N2':^33}|{'N3':^33}|")
    print(delimer)
    print(f"|{' ' * 12}|{'Время':^20}|{'Перестановки':^12}|{'Время':^20}|{'Перестановки':^12}|{'Время':^20}|{'Перестановки':^12}|")
    print(delimer)
    print(
        f"|{'sort':^12}|{format_time(args['t1']):^20}|{args['k1']:^12.6g}|{format_time(args['t2']):^20}|{args['k2']:^12.6g}|{format_time(args['t3']):^20}|{args['k3']:^12.6g}|")
    print(delimer)
    print(
        f"|{'random':^12}|{format_time(args['t4']):^20}|{args['k4']:^12.6g}|{format_time(args['t5']):^20}|{args['k5']:^12.6g}|{format_time(args['t6']):^20}|{args['k6']:^12.6g}|")
    print(delimer)
    print(
        f"|{'reverse sort':^12}|{format_time(args['t7']):^20}|{args['k7']:^12.6g}|{format_time(args['t8']):^20}|{args['k8']:^12.6g}|{format_time(args['t9']):^20}|{args['k9']:^12.6g}|")
    print(delimer)
