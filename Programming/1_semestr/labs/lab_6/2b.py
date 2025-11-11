"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Удалить элемент с заданным индексом алгоритмически.
"""

while True:
    # Ввод данных
    mas = list(map(int, input('Введите список через пробел: ').split()))
    if len(mas) == 0:
        # Проверка на пустоту
        print('List is Empty')
        continue
    i = int(input('Введите индекс элемента, который необходимо удалить: '))
    # Если индекс выходит за границы массива, выводим ошибку
    if i >= len(mas) or i < 0:
        print('Index out of range')
        continue

    # Перестановка элементов
    for j in range(i, len(mas) - 1):
        mas[j] = mas[j + 1]

    # Удаление лишнего элемента
    mas.pop()

    # Вывод массива
    print(f'Result: {mas}')
