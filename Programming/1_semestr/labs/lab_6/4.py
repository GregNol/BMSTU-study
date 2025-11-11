"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Найти наиболее длинную непрерывную последовательность по варианту
Возрастающая последовательность отрицательных чисел, модуль которых является простым числом.
"""

# Генератор простых чисел
simple = [1 for _ in range(pow(10, 7))]
for i in range(2, pow(10, 7)):
    if simple[i] == 1:
        for j in range(2 * i, pow(10, 7), i):
            simple[j] = 0
while True:
    # Ввод данных
    mas = list(map(int, input('Введите список через пробел: ').split()))
    if len(mas) == 0:
        # Проверка на пустоту
        print('List is Empty')
        continue
    max_len = 0 # Максимальная длина последовательности
    local_len = 0 # Длина локальной последовательности
    left = 0 # Индекс начала последовательности максимальной длины
    # Проверяем первый элемент
    if mas[0] < 0 and simple[abs(mas[0])]:
        local_len += 1
        max_len = 1
        left = 0

    # Перебор массива
    for i in range(1, len(mas)):
        if ((mas[i - 1] < mas[i] < 0 < local_len) or (mas[i] < 0 == local_len)) and simple[abs(mas[i])]:
            # Если удовлетворяет условию, добавляем элемент в локальную подпоследовательность
            local_len += 1
            if local_len > max_len:
                max_len = local_len
                left = i - max_len + 1
        else:
            # Если неудовлетворяет, сбрасываем локальную подпоследовательность
            local_len = 0


    # Вывод результата
    print(f'Максимальная длина последовательности: {max_len}')
    print(f'Последовательность: ', end='')
    for i in range(left, left + max_len):
        print(mas[i], end=' ')
    print()
