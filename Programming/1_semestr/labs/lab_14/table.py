from is_numeric import is_int, is_float
import os
import struct
import re

FMT = ''
DELIMITER = ','
FILE_PATH = ''


def print_info():
    """
    Выводит информацию о доступных командах.
    """
    print()
    print(f'Разделитель в таблице: "{DELIMITER}"')
    print('Доступные команды:')
    print('1. select - выбрать таблицу')
    print('2. create - создать таблицу')
    print('3. print_pack - вывести таблицу в бинарном формате')
    print('4. print_unpack - вывести таблицу в string формате')
    print('5. append - добавить строку в таблицу')
    print('6. insert - добавить строку в таблицу на конкретное место')
    print('7. delete - удалить строку из таблицы по id')
    print('8. find_one - найти строки по одному ключу в одном столбце')
    print('9. find_two - найти строки по двум ключам в двух столбцах')
    print('10. set_delimiter - изменить разделитель в таблице')
    print('11. exit - выйти из программы')
    print()


def format_element(el):
    """
    Форматирует элемент таблицы для вывода.
    """
    if type(el) in [int, float]:
        el = int(el)
        return f'{el:^20.6g}'
    if type(el) == bytes:
        el = el.decode('utf-8')
        return f'{el:^20}'
    el = str(el)
    return f'{el:^20}'


def new_fmt(fmt):
    global FMT
    r = r'([if]|[1-9][0-9]*s)*'
    if re.fullmatch(r, fmt):
        FMT = fmt
        return True
    else:
        FMT = ''
        print('Вы ввели неккоректный формат.')
        return False


def validate(row: list):
    fmt = ''
    if FMT == '':
        return False
    for f in FMT:
        if f not in '0123456789':
            fmt += f
    if len(fmt) == len(row):
        res = []
        for i in range(len(row)):
            if fmt[i] == 'i':
                res.append(int(row[i]))
            elif fmt[i] == 'f':
                res.append(float(row[i]))
            elif fmt[i] == 's':
                res.append(str(row[i]).encode('utf-8'))
            else:
                return False
        return res
    return False


def print_pack():
    """
    Выводит текущую таблицу в бинарном виде.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    file = open(FILE_PATH, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    if file_size == 0:
        print('Таблица пуста.')
        file.close()
        return True
    file.seek(0)
    row_len = struct.calcsize(FMT)
    cnt = 0
    row_delimiter = '-' * (row_len * 4 + 4)
    print(row_delimiter)
    while file_size > 0:
        row = file.read(row_len)
        print('|' + f'{str(row):^{row_len * 4 + 2}}' + '|')
        print(row_delimiter)
        cnt += 1
        file_size -= row_len

    print()
    print(f'Всего {cnt:.6g} элементов.')
    file.close()
    return True


def print_unpack():
    """
    Выводит текущую таблицу в обычном виде.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    file = open(FILE_PATH, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    if file_size == 0:
        print('Таблица пуста.')
        file.close()
        return True
    file.seek(0)
    row_len = struct.calcsize(FMT)
    cnt = 0
    row_delimiter = '-' * \
        ((FMT.count('i') + FMT.count('f') + FMT.count('s')) * 21 + 1)
    print(row_delimiter)
    while file_size > 0:
        row = file.read(row_len)
        row = struct.unpack(FMT, row)
        print('|' + '|'.join(list(map(format_element, row))) + '|')
        print(row_delimiter)
        cnt += 1
        file_size -= row_len

    print()
    print(f'Всего {cnt:.6g} элементов.')
    file.close()
    return True


def select(path):
    """
    Выбирает таблицу по заданному пути.
    """
    if not os.path.isfile(path):
        print(f'Файла "{path}" не существует.')
        return ''
    file = open(path, 'r')
    try:
        file.readline()
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {error}')
        file.close()
        return ''
    print('Таблица успешно выбрана.')
    file.close()
    return path


def create(path):
    """
    Создает таблицу по заданному пути с указанными столбцами.
    """
    if os.path.isfile(path):
        os.remove(path)

    file = open(path, 'w')
    print('Таблица успешно инициализирована.')
    file.close()
    return path


def set_delimiter(new_delim):
    """
    Изменяет глобальный `DELIMITER`.
    Поддерживает специальный ввод '\\t' или 'tab' для символа табуляции.
    """
    global DELIMITER
    if not new_delim:
        print('Разделитель не может быть пустым.')
        return None
    if new_delim == '\\t' or new_delim.lower() == 'tab':
        new_value = '\t'
    else:
        new_value = new_delim

    DELIMITER = new_value
    display = "\\t" if DELIMITER == '\t' else DELIMITER
    print(f'Разделитель успешно изменён на: "{display}"')
    return DELIMITER


def find_one(column_id, key):
    """
    Находит строки, где значение в столбце равно ключу.
    """
    if FILE_PATH == '' or FMT == '':
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    file = open(FILE_PATH, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    if file_size == 0:
        print('Таблица пуста.')
        file.close()
        return True
    file.seek(0)
    row_len = struct.calcsize(FMT)
    cnt = 0
    row_delimiter = '-' * \
        ((FMT.count('i') + FMT.count('f') + FMT.count('s')) * 21 + 1)
    print(row_delimiter)
    while file_size > 0:
        row = file.read(row_len)
        row = struct.unpack(FMT, row)
        if row[column_id] == key:
            print('|' + '|'.join(list(map(format_element, row))) + '|')
            print(row_delimiter)
            cnt += 1
        file_size -= row_len

    print()
    print(f'Найдено {cnt:.6g} элементов.')
    file.close()
    return True


def find_two(column_id_1, key_1, column_id_2, key_2):
    """
    Находит строки, где значения в двух столбцах равны заданным ключам.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    file = open(FILE_PATH, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    if file_size == 0:
        print('Таблица пуста.')
        file.close()
        return True
    file.seek(0)
    row_len = struct.calcsize(FMT)
    cnt = 0
    row_delimiter = '-' * \
        ((FMT.count('i') + FMT.count('f') + FMT.count('s')) * 21 + 1)
    print(row_delimiter)
    while file_size > 0:
        row = file.read(row_len)
        row = struct.unpack(FMT, row)
        if row[column_id_1] == key_1 and row[column_id_2] == key_2:
            print('|' + '|'.join(list(map(format_element, row))) + '|')
            print(row_delimiter)
            cnt += 1
        file_size -= row_len

    print()
    print(f'Найдено {cnt:.6g} элементов.')
    file.close()
    return True


def _prepare_data(el):

    if is_int(el):
        el = int(el)
        return el
    elif is_float(el):
        el = float(el)
        return el
    else:
        el = str(el)
        return bytes(el, 'utf-8')


def append(row):
    """
    Добавляет строку в таблицу.
    """
    if FILE_PATH == '' or FMT == '':
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    row = struct.pack(FMT, *row)

    file = open(FILE_PATH, 'ab')
    file.write(row)
    file.close()
    print('Строка была успешно записана в таблицу:')
    return True


def insert(id_column, row: list):
    if FILE_PATH == '' or FMT == '':
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    len_row = struct.calcsize(FMT)
    write_pos = id_column * len_row

    row = struct.pack(FMT, *row)

    file = open(FILE_PATH, 'r+b')
    # print('Открыли файл')
    file.seek(0, 2)  # в конец
    file_size = file.tell()
    # print('Узнали длину файла')
    if write_pos > file_size:
        print('id строки вышел за пределы файла.')
        return None
    new_size = file_size + len_row
    file.truncate(new_size)
    # print('Расширили файл')
    src = file_size - len_row
    while src >= write_pos:
        file.seek(src)
        buf = file.read(len_row)

        file.seek(src + len_row)
        file.write(buf)

        src -= len_row

    # Пишем вставляемые байты
    file.seek(write_pos)
    file.write(row)
    # print('Вставили новую строку')
    file.close()
    print('Строка была успешно записана в таблицу.')
    return True


def delete(id_row):
    """
    Удаляет i-ую строку из таблицы.
    """
    if FILE_PATH == '' or FMT == '':
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    len_row = struct.calcsize(FMT)
    delete_pos = id_row * len_row

    file = open(FILE_PATH, 'r+b')
    file.seek(0, 2)
    file_size = file.tell()

    if file_size == 0:
        print('Таблица пуста.')
        file.close()
        return None

    if delete_pos >= file_size:
        print('id строки вышел за пределы файла.')
        file.close()
        return None

    # Сдвигаем все строки после удаляемой на одну позицию назад
    src = delete_pos + len_row
    while src < file_size:
        file.seek(src)
        buf = file.read(len_row)

        file.seek(src - len_row)
        file.write(buf)

        src += len_row
    new_size = file_size - len_row
    file.truncate(new_size)
    file.close()
    print('Строка была успешно удалена из таблицы.')
    return True


def input_comand():
    """
    Обрабатывает ввод команды пользователя.
    """
    try:
        global FILE_PATH
        comand = input('Введите команду: ').split()
        if not comand:
            print('Команда не распознана. Попробуйте еще раз.')
            return None
        cmd = comand[0]
        if len(comand) > 1:
            print('Команды не поддерживают аргументы при вызове.')

        if cmd == 'select':
            file_path = input('Введите путь до файла: ')
            if file_path == '':
                print('Ошибка ввода.')
                return None
            FILE_PATH = select(file_path)
            if FILE_PATH == '':
                return None
            fmt = input('Введите новый формат: ')
            new_fmt(fmt)
            return True

        elif cmd == 'create':
            file_path = input('Введите путь до файла: ')
            if file_path == '':
                print('Ошибка ввода.')
                return None
            FILE_PATH = create(file_path)
            if file_path == '':
                return None
            fmt = input('Введите новый формат: ')
            new_fmt(fmt)
            return FILE_PATH

        elif cmd == 'append':
            row = input(
                f'Введите строку для добавления, разделитель "{DELIMITER}": ').split(DELIMITER)
            if not row:
                print('Ошибка ввода')
                return None
            row = validate(row)
            if not row:
                print('Строка не соответствует формату')
                return None
            return append(row)

        elif cmd == 'insert':
            row = input(
                f'Введите строку для добавления, разделитель "{DELIMITER}": ').split(DELIMITER)
            if not row:
                print('Ошибка ввода')
                return None
            row = validate(row)
            if not row:
                print('Строка не соответствует формату')
                return None
            column_id = int(
                input('Введите id строки, куда надо вставить строку: '))
            if column_id < 0:
                print('id должно быть натуральным числом')
                return None
            return insert(column_id, row)

        elif cmd == 'find_one':
            column_id = int(input('Введите id столбца для поиска: '))
            key = input('Введите ключ для поиска: ')
            if key == '':
                print('Ошибка ввода.')
                return None
            key = _prepare_data(key)
            return find_one(column_id, key)

        elif cmd == 'find_two':
            column_id_1 = int(input('Введите id первого столбца для поиска: '))
            key_1 = input('Введите ключ для поиска: ')
            if key_1 == '':
                print('Ошибка ввода.')
                return None
            column_id_2 = int(input('Введите id второго столбца для поиска: '))
            key_2 = input('Введите ключ для поиска: ')
            if key_1 == '':
                print('Ошибка ввода.')
                return None
            key_1 = _prepare_data(key_1)
            key_2 = _prepare_data(key_2)
            return find_two(column_id_1, key_1, column_id_2, key_2)

        elif cmd == 'set_delimiter':
            new_delimiter = input('Введите новое значение разделителя.')
            return set_delimiter(new_delimiter)

        elif cmd == 'print_pack':
            return print_pack()

        elif cmd == 'print_unpack':
            return print_unpack()

        elif cmd == 'delete':
            id_row = int(input('Введите id строки для удаления: '))
            if id_row < 0:
                print('id должно быть натуральным числом')
                return None
            return delete(id_row)
        elif cmd == 'exit':
            print('Завершение работы программы.')
            exit()

        else:
            print('Команда не распознана. Попробуйте еще раз.')
            return None
    except PermissionError as error:
        print(f'В процессе выполнения произошла ошибка доступа.')
        return None
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {str(error)}')
        return None
