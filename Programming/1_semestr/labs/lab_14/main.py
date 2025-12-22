"""
Титов Матвей Алексеевич ИУ7-12Б
Назначение: Продемонстрировать работу с бинарными базами данных, реализовать CLI содель взаимодействия
"""

from table import print_info, input_comand


def main():
    print('Перед началом работы выберите или создайте таблицу.')
    while True:
        print_info()
        input_comand()
        input_comand()
        input_comand()


if __name__ == "__main__":
    main()
