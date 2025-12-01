from function import y, y_first


def right_rect(f, a: float, b: float, n: int) -> float:
    # Подсчет интеграла методом правых прямоугольников
    h = (b - a) / n
    i = a + h
    s = 0
    while i <= b:
        s += f(i) * h
        i += h
    return s


def simpson(f, a, b, n):
    # Подсчет интеграла методом парабол - Симпмона
    h = (b - a) / n
    xs = [a + i*h for i in range(n+1)]
    ys = [f(xi) for xi in xs]
    S = ys[0] + ys[-1]
    S += 4 * sum(ys[i] for i in range(1, n, 2))
    S += 2 * sum(ys[i] for i in range(2, n-1, 2))
    return S * h / 3


def integral(a, b):
    return y_first(b) - y_first(a)
