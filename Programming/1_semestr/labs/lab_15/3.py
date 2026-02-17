"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Реализовать сортировку внутри файла
"""

import os
import struct

try:
    # Ввод пути
    while True:
        path = input('Введите путь до файла: ')
        if os.path.isdir(path):
            print('Путь некорректен.')
            continue
        break
    if os.path.isfile(path):
        os.remove(path)

    # Запись данных
    print('Введите целочисленные 32-битные числа, для окончания ввода введите пустую строку: ')
    with open(path, 'wb') as file:
        while True:
            n_input = input()
            if not n_input:
                break
            n = int(n_input)
            file.write(struct.pack('i', n))

    n_size = struct.calcsize('i')
    file_size = os.path.getsize(path)
    count = file_size // n_size  # Количество чисел в файле

    # Сортировка пузырьком внутри файла
    if count > 1:
        with open(path, 'r+b') as file:
            for i in range(count):
                swapped = False
                for j in range(count - i - 1):
                    # Переходим к позиции текущего элемента
                    file.seek(j * n_size)

                    # Читаем два соседних элемента
                    byte_data1 = file.read(n_size)
                    byte_data2 = file.read(n_size)

                    n1 = struct.unpack('i', byte_data1)[0]
                    n2 = struct.unpack('i', byte_data2)[0]

                    # Если левый больше правого — меняем их местами в файле
                    if n1 > n2:
                        # Возвращаемся к началу пары
                        file.seek(j * n_size)
                        # Записываем их в обратном порядке
                        file.write(struct.pack('i', n2))
                        file.write(struct.pack('i', n1))
                        swapped = True

                # Если за проход не было ни одной перестановки, файл отсортирован
                if not swapped:
                    break
    # Вывод результатов
    print('Итоговый файл:')
    with open(path, 'rb') as file:
        while True:
            chunk = file.read(n_size)
            if not chunk:
                break
            n = struct.unpack('i', chunk)[0]
            print(n)

except ValueError:
    print("Ошибка: Введено не целое число.")
except Exception as e:
    print(f'Произошла ошибка в процессе выполнения: {e}')