from random import randint
from datetime import datetime
import time

# Количество перестановок
cnt = 0


def heapify(arr: list, n: int, i: int):
    global cnt

    # Двигает меньший элемент вниз по дереву
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        cnt += 1
        heapify(arr, n, largest)


def heapsort(arr: list):
    global cnt
    n = len(arr)

    # Подготовка дерева
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Перестановка максимума дерева в конец массива
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        cnt += 1
        heapify(arr, i, 0)


def heapsort_random(n):
    """
    Сортировка массива из случайных элементов
    """

    global cnt
    cnt = 0
    arr = [randint(-10**7, 10 ** 8) for _ in range(n)]
    start = time.perf_counter()
    heapsort(arr)
    end = time.perf_counter()
    # print(end - start)
    return end - start, cnt


def heapsort_sorted(n):
    """
    Сортировка отсортированного по возрастанию массива
    """
    global cnt
    cnt = 0
    arr = [i for i in range(1, n + 1)]
    start = time.perf_counter()
    heapsort(arr)
    end = time.perf_counter()
    # print(end-start)
    return end - start, cnt


def heapsort_reverse_sorted(n):
    """
    Сортировка отсортированного по убыванию массива
    """
    global cnt
    cnt = 0
    arr = [i for i in range(n, 0, -1)]
    start = time.perf_counter()
    heapsort(arr)
    end = time.perf_counter()
    # print(end-start)
    return end - start, cnt
