from is_numeric import *

# text = [
#     'Спрятали тележку, и, прихватив одеяла, поднялись по каменистому откосу,',
#     'и устроили наблюдательный пункт, откуда дорога сквозь частокол деревьев',
#     'просматривалась­ не меньше чем на полмили. Расположились с подветрен­ной',
#     'стороны, и закутались поплотнее в одеяла, и по очереди дежурили. Мальчик 5*',
#     '7не выдержал, уснул. Отец и сам уже начал засыпать, как вдруг увидел',
#     'фигуру человека, остановившегося на взгорке посреди дороги. Вскоре появились',
#     'еще двое. И четвертый. Сбились в кучу, постояли. Потом пошли вперед. В',
#     'сумерках он с трудом их различал. Испугался, что они решат встать поблизости',
#     'на ночлег, пожалел, что не нашел места подальше от дороги. Если останутся',
#     'на мосту, им с мальчиком предстоит долгая опасная ночь. 5-3 2*2'
# ]

text = [
    "sneg",
    ".",
    "      ",
    "&nbsp . 5 - 5 * 3"
]

info = 'Список команд:\n' \
    'left - выровнять по левому краю\n' \
    'right - выровнять по правому краю\n' \
    'midlle - выровнять текст по ширине\n' \
    'delete [элемент] - удалить элемент во всем тексте\n' \
    'replace [исходное слово] [заменить на слово] - замена слова во всем слове\n' \
    'math - вычисление операций -|* над числами в тексте\n' \
    'popular - вывод моды каждого предложения\n' \
    'exit - выход из программы'


format_of_print_text = 'left'


def print_info():
    print(info)
    print()


def print_text():
    print()
    print(*text, sep='\n')
    print()


def format_text():
    """
    Форматирует текст после преобразований в установленный формат
    """
    global format_of_print_text
    left()
    if format_of_print_text == 'right':
        right()
    elif format_of_print_text == 'midlle':
        midlle()


def left():
    """
    Выравнивает текст по левому краю
    """
    for j in range(len(text)):
        text[j] = ' '.join(text[j].split())


def right():
    """
    Выравнивает текст по правому краю
    """
    row_len = max(list(map(len, text)))
    for i in range(len(text)):
        text[i] = ' ' * (row_len - len(text[i])) + text[i]


def midlle():
    """
    Выравнивает текст по ширине
    """
    row_len = max(list(map(len, text)))
    for j in range(len(text)):
        row = list(text[j])
        if len(row) == 0:
            row = [' ']
        while len(''.join(row)) < row_len:
            for i in range(len(row)):
                if len(''.join(row)) < row_len:
                    if ' ' in row[i]:
                        row[i] += ' '
                    else:
                        row += ' '
        text[j] = ''.join(row)


def delete(word):
    """
    Удаляет все вхождения слова из текста
    """
    left()
    cnt = 0
    for j in range(len(text)):
        row = text[j]
        while word in row:
            row = row.replace(word, '', 1)
            cnt += 1
        text[j] = row
    format_text()
    print_text()
    print(f'Удалено {cnt:.6g} элементов.')


def replace(old_word, new_word):
    """
    Заменяет все вхождения слова в тексте на новое слово
    """
    left()
    cnt = 0
    for j in range(len(text)):
        row = text[j]
        while old_word in row:
            row = row.replace(old_word, new_word, 1)
            cnt += 1
        text[j] = row
    format_text()
    print_text()
    print(f'Выполнено {cnt:.6g} замен.')


def math():
    """
    Выполняет операции вычитания и умножения над целыми числами в тексте
    """
    cnt = 0
    operators = ['*', '-']
    for i in range(len(text) - 1):
        for operator in operators:
            row = text[i] + text[i + 1]
            element_cnt_1 = len(text[i].split())
            while operator in row:
                pos = row.find(operator)
                if pos == -1:
                    break

                # Находим левое число (идём влево от оператора)
                left_start = pos - 1

                # Пропускаем пробелы слева
                while left_start >= 0 and row[left_start] == ' ':
                    left_start -= 1

                if left_start < 0:
                    break

                # Находим начало числа
                left_end = left_start
                while left_start >= 0 and (is_int(row[left_start])):
                    left_start -= 1

                # Проверяем на отрицательное число
                if left_start >= 0 and row[left_start] == '-':
                    # Проверяем, что это минус числа, а не оператор
                    if left_start == 0 or not is_int(row[left_start - 1]):
                        left_start -= 1

                left_start += 1

                # Проверяем, что нашли число
                num1_str = row[left_start:left_end + 1].strip()
                if not is_int(num1_str):
                    break

                # Находим правое число (идём вправо от оператора)
                right_start = pos + 1

                # Пропускаем пробелы справа
                while right_start < len(row) and row[right_start] == ' ':
                    right_start += 1

                if right_start >= len(row):
                    break

                # Проверяем на отрицательное число справа
                right_end = right_start

                # Находим конец числа
                while right_end < len(row) and (is_int(row[right_end])):
                    right_end += 1

                # Проверяем, что нашли число
                num2_str = row[right_start:right_end].strip()
                if not is_int(num2_str):
                    break

                # Преобразуем строки в числа
                num1 = int(num1_str)
                num2 = int(num2_str)

                # Вычисляем результат
                if operator == '*':
                    result_value = num1 * num2
                else:  # operator == '-'
                    result_value = num1 - num2

                # Форматируем результат
                result_str = f' {result_value:.6g} '

                # Заменяем выражение на результат
                row = row[:left_start] + result_str + row[right_end:]
                cnt += 1
                row = row.strip()
                text[i] = ' '.join(row.split()[:element_cnt_1])
                text[i + 1] = ' '.join(row.split()[element_cnt_1:])
    format_text()
    print_text()
    print(f'Выполнено {cnt:.6g} замен.')


def popular():
    """
    Выводит наиболее часто встречающиеся слова в каждом предложении
    """
    line = ''
    ind = 0
    for i in range(len(text)):
        row = text[i]
        row += ' '

        # Набираем в переменную line преложение
        for l in row:
            if l != '.':
                line += l
            else:

                # Считаем сколько раз встречается каждое слово в предложении
                line = line.replace(',', '')
                line = line.split()
                words = {}
                for word in line:
                    word = word.lower()
                    if word in words.keys():
                        words[word] += 1
                    else:
                        words[word] = 1

                # Выводим самые частовстречающиеся слова в каждом предложении
                max_count = max(words.values())
                popular_words = [el for el,
                                 count in words.items() if count == max_count]
                print(
                    f'В предложении {ind + 1} наиболее популярные слова: {", ".join(popular_words)}')
                line = ''
                ind += 1
    format_text()
    print_text()


def input_comand():
    cmd = input()
    if cmd in ['left', 'right', 'midlle']:
        global format_of_print_text
        format_of_print_text = cmd
        format_text()
        print_text()
    elif 'delete' in cmd:
        cmd = cmd.split()
        if len(cmd) == 2:
            delete(cmd[1])
        else:
            print('Вы ввели более одного слова для удаления')
    elif 'replace' in cmd:
        cmd = cmd.split()
        if len(cmd) == 3:
            replace(cmd[1], cmd[2])
        else:
            print('Вы ввели более двух слов')
    elif cmd == 'math':
        math()
    elif cmd == 'popular':
        popular()
    elif cmd == 'exit':
        exit()
    else:
        print('Вы ввели недопустимую команду.')
