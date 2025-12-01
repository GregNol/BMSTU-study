from is_numeric import is_int, is_float

delimiter = ','
file_path = None


def select(path):
    file = open(path, 'r')
    if not file:
        print('Такого файла не существует или таблица пуста.')
        return None
    try:
        columns = file.readline().rstrip().split(delimiter)
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {error}')
        file.close()
        return None
    print('Таблица успешно выбрана.')
    print(f'Поля таблицы: {columns}')
    return path


def create(path, columns):
    if not columns:
        print('Таблица не может существовать без столбцов.')
        return None
    try:
        file = open(path, 'w')
        file.write(delimiter.join(columns))
    except Exception as error:
        print(f'В процессе выполнения произошла ошибка: {error}')
        return None
    print('Таблица успешно инициализирована.')
    file.close()
    return path


def format_element(el):
    if is_int(el):
        el = int(el)
        return f'{el:^20.6g}'
    if is_float(el):
        el = float(el)
        return f'{el:^20.6g}'
    return f'{el:^20}'


def print_table():
    if file_path is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    file = open(file_path, 'r')
    columns = file.readline().rstrip().split(delimiter)
    row_delimiter = '-' * (len(columns) * 21 + 1)
    print(row_delimiter)
    print('|' + '|'.join(list(map(format_element, columns))) + '|')
    print(row_delimiter)
    cnt = 0
    for row in file.readlines():
        row = row.rstrip().split(delimiter)
        print('|' + '|'.join(list(map(format_element, row))) + '|')
        print(row_delimiter)

        cnt += 1

    print()
    print(f'Всего {cnt:.6g} элементов.')
    file.close()
    return True


def append(row):
    if file_path is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None
    row = row.split(delimiter)
    file = open(file_path, 'r')
    columns = file.readline().rstrip().split(delimiter)
    file.close()

    if len(columns) == len(row):
        file = open(file_path, 'a')
        file.write(delimiter.join(row))
        file.close()
        print('Строка была успешно записана в таблицу:')
        return True
    else:
        print('Количество элементов в введенной строке не соответствует количеству элементов в таблице.')
        return None


def find_one(column, key):
    if file_path is None:
        print('Перед началом работы, выберете таблицу или инициализируйте её.')
        return None

    file = open(file_path, 'r')
    columns = file.readline().rstrip().split(delimiter)
    if column not in columns:
        print('Введенное поле не существует в таблице.')
        file.close()
        return None

    column_id = columns.index(column)
    row_delimiter = '-' * (len(columns) * 21 + 1)
    print(row_delimiter)
    cnt = 0
    for row in file.readlines():
        row = row.rstrip().split(delimiter)
        if row[column_id] == key:
            print('|' + '|'.join(list(map(format_element, row))) + '|')
            print(row_delimiter)
            cnt += 1

    print()
    print(f'Найдено {cnt:.6g} элементов.')
