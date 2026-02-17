"""
Титов Матвей Алексеевич
Назначение: Запись удвоенного значения отрицательных элементов
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
    print('Введите целочисленные 32-битные в разных строках, для окончания ввода введите пустую строку: ')
    file = open(path, 'wb')
    n = input()
    while n:
        n = int(n)
        file.write(struct.pack('i', n))
        n = input()
    file.close()
    n_size = struct.calcsize('i')

    # Подсчет отрицательных чисел
    neg_count = 0
    with open(path, 'rb') as file:
        while True:
            n = file.read(n_size)
            if not n:
                break
            n = struct.unpack('i', n)[0]
            if n < 0:
                neg_count += 1

    # Подсчет нового размера
    original_size = os.path.getsize(path)
    new_size = original_size + neg_count * n_size

    with open(path, 'r+b') as file:
        # Увеличиваем файл до нужного размера
        file.truncate(new_size)

        # read_pos — откуда берем число (конец старых данных)
        # write_pos — куда записываем число (конец расширенного файла)
        read_pos = original_size - n_size
        write_pos = new_size - n_size

        # Чтение и смещение с конца
        while read_pos >= 0:
            # Читаем число из старой позиции
            file.seek(read_pos)
            n = struct.unpack('i', file.read(n_size))[0]

            if n < 0:
                # Если число отрицательное, записываем в новую позицию его удвоенное значение и перед ним само число
                product = 2 * n

                file.seek(write_pos)
                file.write(struct.pack('i', product))
                write_pos -= n_size

                file.seek(write_pos)
                file.write(struct.pack('i', n))
                write_pos -= n_size
            else:
                # Если положительное, записываем в новую позицию
                file.seek(write_pos)
                file.write(struct.pack('i', n))
                write_pos -= n_size

            read_pos -= n_size

    # Вывод результатов
    print('Итоговый файл:')
    file = open(path, 'rb')
    n = file.read(n_size)
    while n:
        n = struct.unpack('i', n)[0]
        print(n)
        n = file.read(n_size)
except Exception as e:
    print(f'Произошла ошибка в процессе выполнения: {e}')