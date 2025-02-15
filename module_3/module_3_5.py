# Самостоятельная работа по уроку "Рекурсия"

# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает
# произведение цифр этого числа.

# Пункты задачи:
# 1. Напишите функцию get_multiplied_digits и параметр number в ней.
# 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# 3. Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё
# первый символ из str_number в числовом представлении(int).
# 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите
# первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться
# взять срез str_number[1:].
# 5. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

# Пример результата выполнения программы:
# Исходный код:
# result = get_multiplied_digits(40203)
# print(result)
#
# Вывод на консоль:
# 24

# Примечания:
# При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
# Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка
# заключается в бесконечной рекурсии или же в неверном обращении по индексу.

def get_multiplied_digits(number=102030):
    str_number=str(number).replace('0','') # Преобразуем number в строку с удалением нулей
    if len(str_number) == 1:   #!!ПОГРАНИЧНОЕ УСЛОВИЕ РЕКУРСИИ, (базовый случай), с которого начинается возврат стека
        multiplied = int(str_number)
        return multiplied
    else:
        multiplied = int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))
        return multiplied

print(get_multiplied_digits(int(input('Введите любое целое число для вычисления произведения цифр: '))))


# ИТЕРАТИВНЫЙ вариант для этой задачи, по моему, красивее РЕКУРСИВНОГО.
def get_multiplied_digits_iterativ(number=102030):
    str_number = str(number).replace('0', '')  # Преобразуем number в строку с удалением нулей
    multiplied = 1
    for digit in str_number:
        multiplied *= int(digit)
    return multiplied

print(get_multiplied_digits_iterativ())