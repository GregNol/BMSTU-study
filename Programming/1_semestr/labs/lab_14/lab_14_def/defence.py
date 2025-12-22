import struct

try:
    while True:
        print('Введите целочисленную матрицу. Для окончания ввода отправьте пустую строку')
        array = []

        row = input()
        if row:
            row = list(map(int, row.split()))
            len_row = len(row)
            array.append(row)
        else:
            print('Ошибка ввода')
            exit()
        row = input()
        while row:
            row = list(map(int, row.split()))
            if len(row) != len_row:
                print('Ошибка ввода')
                continue
            array.append(row)
            row = input()
        n = len(array)
        file_input = open('input.txt', 'wb')

        for row in array:
            for el in row:
                file_input.write(struct.pack('i', el))
        file_input.close()

        file_input = open('input.txt', 'rb')
        file_output = open('output.txt', 'wb')

        for i in range(len_row):
            for j in range(n):
                file_input.seek(struct.calcsize('i') * (j * len_row + i))
                el = file_input.read(struct.calcsize('i'))
                file_output.write(el)
        file_output.close()

        print('Входные данные')
        file_input.seek(0)
        for _ in range(n):
            el = file_input.read(struct.calcsize('i') * len_row)
            el = struct.unpack('i' * len_row, el)
            print('\t'.join(list(map(str, el))))
        file_input.close()

        print('Результат')
        file_output = open('output.txt', 'rb')
        for _ in range(len_row):
            el = file_output.read(struct.calcsize('i') * n)
            el = struct.unpack('i' * n, el)
            print('\t'.join(list(map(str, el))))
        file_output.close()
except Exception as e:
    print('В процессе выполнения произошла ошибка:', str(e))