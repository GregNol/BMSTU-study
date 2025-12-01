from math import sin, cos


def y(x: float) -> float:
    # Интегрируемая функция
    return cos(x) * (x ** 2) + 2 * sin(x) * x + 10


def y_first(x: float) -> float:
    # Первообразная интегрируемой функции
    return sin(x) * (x ** 2) + 10 * x


def f(x):
    return x ** 2


def g(x):
    return - x ** 2 + 1e4


def get_zero(f, a, b):
    # Находит нули функции на заданном промежутке
    left = a
    right = b
    eps = 1e-8
    func_left = f(left)
    func_right = f(right)
    if func_left * func_right < 0:
        if abs(left - right) >= eps:
            return get_zero(f, left, (left + right) / 2) + get_zero(f, (left + right) / 2, right)
        else:
            return [(left + right) / 2]
    else:
        if abs(left - right) >= 2:
            return get_zero(f, left, (left + right) / 2) + get_zero(f, (left + right) / 2, right)
        else:
            return []
