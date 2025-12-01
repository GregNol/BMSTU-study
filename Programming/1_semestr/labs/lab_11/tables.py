def format_float(n):
    # Форматирование чисел
    if n == 0:
        return '-'
    else:
        return f'{n:.6g}'


def table_results(i1, i1_absolut, i1_relative, i2, i2_absolut, i2_relative, i3, i3_absolut, i3_relative, i4, i4_absolut, i4_relative, n1, n2):
    # Вывод таблицы с результатами
    print()
    delimer = '-' * (16 + 58 * 2)
    print(delimer)
    print(f'|{" "*16}|{f"N1={format_float(n1)}":^56}|{f"N2={format_float(n2)}":^56}|')
    print(delimer)
    print(f'|{" " * 16}|{"integral":^18}|{"absolut":^18}|{"relative":^18}|{"integral":^18}|{"absolut":^18}|{"relative":^18}|')
    print(delimer)
    print(f'|{"Right rect":<16}|{format_float(i1):^18}|{format_float(i1_absolut):^18}|{f"{format_float(i1_relative)}%":^18}|'
          f'{format_float(i2):^18}|{format_float(i2_absolut):^18}|{f"{format_float(i2_relative)}%":^18}|')
    print(delimer)
    print(f'|{"Simpson":<16}|{format_float(i3):^18}|{format_float(i3_absolut):^18}|{f"{format_float(i3_relative)}%":^18}|'
          f'{format_float(i4):^18}|{format_float(i4_absolut):^18}|{f"{format_float(i4_relative)}%":^18}|')
    print(delimer)
    print()
