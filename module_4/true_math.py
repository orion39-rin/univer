from math import inf

def divide(first, second):
    """
    Функция должна возвращать результат деления first на second,
    но когда в second записан 0 - возвращать бесконечность из встроенной библиотеки math.
    """
    if second > 0:
        div = first / second
    else:
        return inf

    return div

# Локальное тестирование функции.
if __name__ == '__main__':
    help(divide)
    print(divide(258, 369))
    print(divide(258, 0))
