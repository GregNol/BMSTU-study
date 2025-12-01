"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Продемонстрировать работу со строковыми данными, реализовать CLI содель взаимодействия
"""

import word
from word import text


def main():
    if len(text) == 0:
        print('Текст отсутствует. Завершение работы программы.')
        return
    # Вывод текста
    word.print_text()
    while True:
        # Работа программы
        word.print_info()
        word.input_comand()
        word.input_comand()
        word.input_comand()


if __name__ == "__main__":
    main()
