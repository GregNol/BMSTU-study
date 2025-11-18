def is_int(n):
    """
    Проверка является ли строка целым числом или массив целочисленным
    :param n: проверяемая строка/массив
    :return: True - число целое/массив целочисленный; False - в остальных случаях
    """
    numbers = '0123456789'
    numbers_first = '0123456789-+'

    if len(n) == 0:
        print('Введена пустая строка')
        return False
    if type(n) == str:
        """
        Перебираем все символы строки, каждый из них должен быть цифрой
        """
        if n[0] not in numbers_first:
            print(f'{n} - не является целым числом')
            return False
        if n[0] == '-' and len(n) == 1:
            print(f'{n} - не является целым числом')
            return False
        for i in range(1, len(n)):
            if n[i] in numbers:
                continue
            else:
                print(f'{n} - не является целым числом')
                return False
        return True
    else:
        """
        Перебираем все элементы массива, каждый из них должен входить быть числом
        """
        for i in n:
            if is_int(i):
                continue
            else:
                return False
        return True


def is_float(n):
    """
        Проверка является ли строка числом или массив численным
        :param n: проверяемая строка/массив
        :return: True - строка является числом/численным массивом; False - в остальных случаях
        """
    numbers = '0123456789.'
    numbers_first = '0123456789-+'

    if len(n) == 0:
        print('Введена пустая строка')
        return False
    if type(n) == str:
        """
        Перебираем все символы строки, каждый из них должен быть цифрой, либо точкой - разделитель целой и добной части
        Также проверяем, чтобы в числе была максимум одна точка и она находилась не на первом и не последнем месте
        """
        # n = list(n)
        cnt_dot = 0
        if n[-1] == '.':
            print(f'{n} - не является числом')
            return False
        if n[0] not in numbers_first:
            print(f'{n} - не является числом')
            return False
        if n[0] == '-' and len(n) == 1:
            print(f'{n} - не является целым числом')
            return False
        for i in range(1, len(n)):
            if n[i] == '.':
                cnt_dot += 1
                if cnt_dot > 1:
                    print(f'{n} - не является числом')
                    return False
            if n[i] in numbers:
                continue
            else:
                print(f'{n} - не является числом')
                return False
        return True
    else:
        """
        Перебираем все элементы массива, каждый из них должен входить быть числом
        """
        for i in n:
            if is_float(i):
                continue
            else:
                return False
        return True
