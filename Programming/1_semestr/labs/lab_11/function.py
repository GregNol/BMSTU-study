from math import sin, cos


def y(x: float) -> float:
    # Интегрируемая функция
    return cos(x) * (x ** 2) + 2 * sin(x) * x + 10


def y_first(x: float) -> float:
    # Первообразная интегрируемой функции
    return sin(x) * (x ** 2) + 10 * x
