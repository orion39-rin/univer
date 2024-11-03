
def divide(first, second):
    """
    Функция должна возвращать результат деления first на second,
    но когда в second записан 0 - возвращать строку 'Ошибка'.
    """
    if second > 0:
        div = first / second
    else:
        div = 'Ошибка'

    return div

# Локальное тестирование функции.
if __name__ == '__main__':
    print(divide(258, 369))
    print(divide(258, 0))