import tempfile
from is_numeric import is_int, is_float
import os
DELIMITER = ','
FILE_PATH = None
datatype_columns = {}


def print_info():
    """
    Выводит информацию о доступных командах.
    """
    print()
    print(f'Разделитель в таблице: "{DELIMITER}"')
    print('Доступные команды:')
    print('1. select PATH - выбрать таблицу по пути')
    print('2. create PATH - создать таблицу по пути с заданными столбцами')
    print('3. print_table - вывести текущую таблицу')
    print('4. append ROW - добавить строку в таблицу')
    print('5. find_one COLUMN KEY - найти строки по одному ключу в одном столбце')
    print('6. find_two COLUMN_1 KEY_1 COLUMN_2 KEY_2 - найти строки по двум ключам в двух столбцах')
    print('7. sort_one COLUMN - отсортировать таблицу по одному полю (по возрастанию)')
    print('8. sort_two COLUMN_1 COLUMN_2 - отсортировать таблицу по двум полям (по возрастанию)')
    print('9. set_delimiter DELIM - изменить разделитель таблицы (use "\\t" or "tab" for tab)')
    print('10. exit - выйти из программы')

    print()


def format_element(el):
    """
    Форматирует элемент таблицы для вывода.
    """
    if is_int(el):
        el = int(el)
        return f'{el:^20.6g}'
    if is_float(el):
        el = float(el)
        return f'{el:^20.6g}'
    return f'{el:^20}'


def print_table():
    """
    Выводит текущую таблицу.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    file = open(FILE_PATH, 'r')
    columns = file.readline().rstrip().split(DELIMITER)
    row_delimiter = '-' * (len(columns) * 21 + 1)
    print(row_delimiter)
    print('|' + '|'.join(list(map(format_element, columns))) + '|')
    print(row_delimiter)
    cnt = 0
    for row in file.readlines():
        row = row.rstrip().split(DELIMITER)
        print('|' + '|'.join(list(map(format_element, row))) + '|')
        print(row_delimiter)

        cnt += 1

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
        return None
    file = open(path, 'r')
    if not file:
        print('Таблица пуста.')
        return None
    try:
        columns = file.readline().rstrip().split(DELIMITER)
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {error}')
        file.close()
        return None
    print('Таблица успешно выбрана.')
    print(f'Поля таблицы: {columns}')
    file.close()
    return path


def create(path, columns):
    """
    Создает таблицу по заданному пути с указанными столбцами.
    """
    if os.path.isfile(path):
        print(f'Файл "{path}" уже существует.')
    if not columns:
        print('Таблица не может существовать без столбцов.')
        return None
    try:
        file = open(path, 'w')
        file.write(DELIMITER.join(columns))
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {error}')
        return None
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


def append(row):
    """
    Добавляет строку в таблицу.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    row = row.split(DELIMITER)
    file = open(FILE_PATH, 'r')
    columns = file.readline().rstrip().split(DELIMITER)
    file.close()

    if len(columns) == len(row):
        file = open(FILE_PATH, 'a')
        file.write('\n' + DELIMITER.join(row))
        file.close()
        print('Строка была успешно записана в таблицу:')
        return True
    else:
        print('Количество элементов в введенной строке не соответствует количеству элементов в таблице.')
        return None


def find_one(column, key):
    """
    Находит строки, где значение в столбце равно ключу.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    file = open(FILE_PATH, 'r')
    columns = file.readline().rstrip().split(DELIMITER)
    if column not in columns:
        print('Введенное поле не существует в таблице.')
        file.close()
        return None

    column_id = columns.index(column)
    row_delimiter = '-' * (len(columns) * 21 + 1)
    print(row_delimiter)
    cnt = 0
    for row in file.readlines():
        row = row.rstrip().split(DELIMITER)
        if row[column_id] == key:
            print('|' + '|'.join(list(map(format_element, row))) + '|')
            print(row_delimiter)
            cnt += 1

    print()
    print(f'Найдено {cnt:.6g} элементов.')
    file.close()
    return True


def find_two(column_1, key_1, column_2, key_2):
    """
    Находит строки, где значения в двух столбцах равны заданным ключам.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    file = open(FILE_PATH, 'r')
    columns = file.readline().rstrip().split(DELIMITER)
    if column_1 not in columns or column_2 not in columns:
        print('Введенное поле не существует в таблице.')
        file.close()
        return None

    column_1_id = columns.index(column_1)
    column_2_id = columns.index(column_2)
    row_delimiter = '-' * (len(columns) * 21 + 1)
    print(row_delimiter)
    cnt = 0
    for row in file.readlines():
        row = row.rstrip().split(DELIMITER)
        if row[column_1_id] == key_1 and row[column_2_id] == key_2:
            print('|' + '|'.join(list(map(format_element, row))) + '|')
            print(row_delimiter)
            cnt += 1

    print()
    print(f'Найдено {cnt:.6g} элементов.')
    file.close()
    return True


def compare_value(a, b):
    """
    Сравнивает два строковых значения с учётом числовых типов.
    Возвращает:
      -1 если a < b
       0 если a == b
       1 если a > b
    """
    if is_int(a) and is_int(b):
        ai = int(a)
        bi = int(b)
        return (ai > bi) - (ai < bi)
    if (is_int(a) or is_float(a)) and (is_int(b) or is_float(b)):
        af = float(a)
        bf = float(b)
        return (af > bf) - (af < bf)
    # fallback to string comparison
    if a == b:
        return 0
    return 1 if a > b else -1


def bubble_sort_file(path, key_indices):
    """
    Выполняет пузырьковую сортировку файла `path` по полям с индексами `key_indices`.
    `key_indices` - list/tuple индексов столбцов по приоритету сравнения.
    Использует временный файл и меняет строки местами при необходимости.
    """
    if not os.path.isfile(path):
        print(f'Файл "{path}" не существует.')
        return None

    # Если в таблице нет данных или только заголовок, ничего не делаем
    while True:
        swapped = False
        with open(path, 'r', encoding='utf-8') as src, tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8', newline='') as tmp:
            header = src.readline()
            if not header:
                # пустой файл
                tmp_name = tmp.name
                tmp.write('')
                tmp.close()
                os.replace(tmp_name, path)
                return True
            # Записываем заголовок (убираем возможные лишние переводы строки и добавляем один)
            tmp.write(header.rstrip('\n') + '\n')

            prev_line = src.readline()
            if not prev_line:
                # нет данных
                tmp_name = tmp.name
                tmp.close()
                os.replace(tmp_name, path)
                return True

            prev_fields = prev_line.rstrip('\n').split(DELIMITER)

            for curr_line in src:
                curr_fields = curr_line.rstrip('\n').split(DELIMITER)

                # Сравниваем по ключам
                cmp = 0
                for idx in key_indices:
                    a = prev_fields[idx] if idx < len(prev_fields) else ''
                    b = curr_fields[idx] if idx < len(curr_fields) else ''
                    cmp = compare_value(a, b)
                    if cmp != 0:
                        break

                if cmp <= 0:
                    # порядок верный: сначала prev, затем продолжаем
                    tmp.write(prev_line.rstrip('\n') + '\n')
                    prev_line = curr_line
                    prev_fields = curr_fields
                else:
                    # нужно поменять местами: пишем curr, затем оставляем prev для сравнения со следующим
                    tmp.write(curr_line.rstrip('\n') + '\n')
                    swapped = True
                    # prev_line остаётся тем же (его сравнят с следующим)

            # В конце записываем последний prev_line
            tmp.write(prev_line.rstrip('\n') + '\n')
            tmp_name = tmp.name

        # Заменяем исходный файл временным
        os.replace(tmp_name, path)

        if not swapped:
            break

    print('Таблица успешно отсортирована.')
    return True


def sort_one(column):
    """
    Сортирует таблицу по одному столбцу (по возрастанию) используя пузырьковую сортировку.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        columns = f.readline().rstrip('\n').split(DELIMITER)

    if column not in columns:
        print('Введенное поле не существует в таблице.')
        return None

    col_idx = columns.index(column)
    return bubble_sort_file(FILE_PATH, [col_idx])


def sort_two(column_1, column_2):
    """
    Сортирует таблицу по двум столбцам (первичное - column_1, вторичное - column_2) по возрастанию.
    """
    if FILE_PATH is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        columns = f.readline().rstrip('\n').split(DELIMITER)

    if column_1 not in columns or column_2 not in columns:
        print('Введенное поле не существует в таблице.')
        return None

    idx1 = columns.index(column_1)
    idx2 = columns.index(column_2)
    return bubble_sort_file(FILE_PATH, [idx1, idx2])


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
            args = comand[1:]
        else:
            args = []

        if cmd == 'select':
            if len(args) > 1:
                args = [" ".join(args)]
            FILE_PATH = select(args[0])
            return
        elif cmd == 'create':
            if len(args) > 1:
                args = [" ".join(args)]
            path = args[0]
            columns = input(
                f'Введите названия столбцов через "{DELIMITER}: "').split(DELIMITER)
            FILE_PATH = create(path, columns)
            return FILE_PATH
        elif cmd == 'append':
            if len(args) == 0:
                print('Неверное количество аргументов для команды append.')
                return None
            if len(args) > 1:
                args = [' '.join(args)]
            return append(args[0])
        elif cmd == 'find_one':
            if len(args) != 2:
                print('Неверное количество аргументов для команды find_one.')
                return None
            return find_one(args[0], args[1])
        elif cmd == 'find_two':
            if len(args) != 4:
                print('Неверное количество аргументов для команды find_two.')
                return None
            return find_two(args[0], args[1], args[2], args[3])
        elif cmd == 'sort_one':
            if len(args) != 1:
                print('Неверное количество аргументов для команды sort_one.')
                return None
            return sort_one(args[0])
        elif cmd == 'sort_two':
            if len(args) != 2:
                print('Неверное количество аргументов для команды sort_two.')
                return None
            return sort_two(args[0], args[1])
        elif cmd == 'set_delimiter':
            if len(args) != 1:
                print('Неверное количество аргументов для команды set_delimiter.')
                return None
            return set_delimiter(args[0])
        elif cmd == 'print_table':
            return print_table()
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
        print(f'В процессе выполнения произошла ошибка: {error}')
        return None
