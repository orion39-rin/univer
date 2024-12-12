#Домашнее задание по теме "Создание исключений"
"""
Задача "Некорректность":"""
'''
Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если 
корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если 
корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, 
которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. 
(тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число 
находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.

__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не 
строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять 
ровно из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении 
атрибутов __vin и __numbers).

Пример результата выполнения программы:
Пример выполняемого кода:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера

Примечания:
Для выбрасывания исключений используйте оператор raise'''
######################################################################################################################

# Исключение для некорректного VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

# Исключение для некорректных автомобильных номеров
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

# Основной класс автомобиля
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model

        # Проверяем vin на корректность при инициализации (vin номер автомобиля (int). Уровень доступа private.)
        if self.__is_valid_vin(vin):
            self.__vin = vin

        # Проверяем номера на корректность при инициализации (Уровень доступа private).
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    # Приватный метод для проверки корректности VIN номера
    def __is_valid_vin(self, vin_number):
        # Проверяем, является ли vin_number целым числом
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        # Проверяем, находится ли vin_number в допустимом диапазоне
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        # Если все проверки пройдены, возвращаем True
        return True

    # Приватный метод для проверки корректности автомобильных номеров
    def __is_valid_numbers(self, numbers):
        # Проверяем, является ли numbers строкой
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        # Проверяем, состоит ли строка numbers ровно из 6 символов
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        # Если все проверки пройдены, возвращаем True
        return True

######################################################################################################################

if __name__ == '__main__':

    try:
      first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{first.model} успешно создан')

    try:
      second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{second.model} успешно создан')

    try:
      third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{third.model} успешно создан')
