"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение:
Дана матрица символов. Преобразовать её следующим образом: заменить все
согласные латинских букв на заглавные, а все гласные латинские буквы на
строчные. Вывести матрицу до преобразования и после
"""

matrix = []

while True:
    # Ввод данных
    matrix = []
    print('Введите матрицу символов. Строки матрицы вводите в разных строках. Ввод матрицы завершите символом "*"')
    row = input()
    n = len(row)
    if n == 0:
        print('Вы ввели пустую строку')
        continue
    matrix.append(list(row))
    f_exit = 0
    while True:
        row = input()
        if row == '*':
            break
        len_row = len(row)
        if len_row == n:
            matrix.append(list(row))
        else:
            print(f'Строка матрицы должна содержать {n} элементов, Вы ввели {len_row} элемента.')
            f_exit = 1
            break
    if f_exit:
        continue

    # Печать матрицы
    matrix_len = len(matrix)
    print()
    print('Входные данные:')
    delimer = '-' * (6 * n + 1)
    print(delimer)
    for i in range(matrix_len):
        print('|', end='')
        for j in matrix[i]:
            print(f'{j:^5}|', end='')
        print()
        print(delimer)


    # Преобразование матрицы
    consonants  = 'zxcvbnmsdfghjklptrwy'
    vowels = 'AQEUIO'
    for i in range(matrix_len):
        for j in range(n):
            if matrix[i][j] in consonants:
                matrix[i][j] = chr(ord(matrix[i][j]) - 32)
            if matrix[i][j] in vowels:
                matrix[i][j] = chr(ord(matrix[i][j]) + 32)


    # Печать матрицы
    matrix_len = len(matrix)
    print()
    print('Результат работы:')
    delimer = '-' * (6 * n + 1)
    print(delimer)
    for i in range(matrix_len):
        print('|', end='')
        for j in matrix[i]:
            print(f'{j:^5}|', end='')
        print()
        print(delimer)
