def number_to_text(num, case='default'):
    """
    Преобразует число в текстовую форму с учётом заданного склонения.

    :param num: Число для преобразования (1, 2, 3 и т.д.) пока до десятки)))
    :param case: Склонение ('default', 'ordinal', 'ordinal-f')
                 'default' - базовое число ('один', 'два', 'три')
                 'ordinal' - порядковое число ('первый', 'второй', 'третий')
                 'ordinal-f' - порядковое число женского рода ('первая', 'вторая', 'третья')
    :return: Текстовое представление числа с указанным склонением
    """
    # Базовые числа
    numbers_default = [
        "ноль", "один", "два", "три", "четыре",
        "пять", "шесть", "семь", "восемь", "девять", "десять"
    ]
    # Порядковые числа мужского рода
    numbers_ordinal = [
        "нулевой", "первый", "второй", "третий", "четвёртый",
        "пятый", "шестой", "седьмой", "восьмой", "девятый", "десятый"
    ]
    # Порядковые числа женского рода
    numbers_ordinal_f = [
        "нулевая", "первая", "вторая", "третья", "четвёртая",
        "пятая", "шестая", "седьмая", "восьмая", "девятая", "десятая"
    ]

    if num < 0 or num > 10:
        raise ValueError("Число должно быть в диапазоне от 0 до 10.")

    if case == 'default':
        return numbers_default[num]
    elif case == 'ordinal':
        return numbers_ordinal[num]
    elif case == 'ordinal-f':
        return numbers_ordinal_f[num]
    else:
        raise ValueError("Неверный параметр 'case'. Используйте 'default', 'ordinal' или 'ordinal-f'.")
