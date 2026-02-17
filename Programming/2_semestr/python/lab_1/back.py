"""
Автор: Титов Матвей Алексеевич ИУ7-12Б
Назначение: Калькулятор
"""


def int_to_base7(num):
    """Преобразовать целое число в 7-ю систему"""
    if num == '0':
        return '0'
    if num[0] == '-':
        return '-' + int_to_base7(num[1:])
    num = int(num)
    digits = []
    while num > 0:
        digits.append(str(num % 7))
        num //= 7

    return ''.join(reversed(digits))


def frac_to_base7(frac, precision=10):
    """Преобразовать дробную часть в 7-ю систему"""
    result = []
    for _ in range(precision):
        frac *= 7
        digit = int(frac)
        result.append(str(digit))
        frac -= digit
        if frac == 0:
            break

    return ''.join(result)


def int_from_base7(num_str):
    """Преобразовать целую часть из 7-й системы"""
    result = 0
    if num_str[0] == '-':
        num_str = num_str[1:]
        return '-' + int_from_base7(num_str)
    for i, char in enumerate(num_str):
        result += int(char) * (7 ** (len(num_str) - 1 - i))
        print(char, result)
    return str(result)


def frac_from_base7(num_str):
    """Преобразовать дробную часть из 7-й системы"""
    result = 0.0
    power = 1
    for digit in num_str[2:]:  # Пропускаем '0.'
        power *= 7
        result += int(digit) / power

    return str(result)[2:]
