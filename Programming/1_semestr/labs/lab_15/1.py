"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: удаление всех положительных чисел
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

    # Удаление положительных файлов
    file = open(path, 'r+b')
    n_size = struct.calcsize('i') + 1
    n = file.read(n_size)
    i = 0
    delta = 0
    while n:
        n = struct.unpack('i', n)[0]
        if n > 0:
            delta += 1
            i += 1
        else:
            file.seek((i - delta) * n_size)
            file.write(struct.pack('i', n))
            i += 1
            file.seek(i * n_size)
        n = file.read(n_size)
    file.truncate((i - delta) * n_size)
    file.close()

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