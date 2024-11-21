# Ваша задача:
# понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.

"""
Дополнительно о работе метода __new__:
Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
Разберёмся, как происходит передача данных между ними на следующем примере:

class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)

Работа __new__:
'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0 как
единственный элемент кортежа.
second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться под
 ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.

Передача данных из __new__ в __init__:
После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
В параметр first распакуется из args единственный аргумент 'data'.
В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
"""


"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам 
класса используя ссылку на сам класс - cls.

Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.


Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также 
значение атрибута houses_history.

Пример результата выполнения программы:

Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории

['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

ЖК Эльбрус снесён, но он останется в истории

Примечания:
В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.
"""
##################################################################################################
class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)

##################################################################################################
class House:
    houses_history = []  # Список для хранения истории созданных домов

    def __new__(cls, *args, **kwargs):
        # Создание нового объекта
        instance = super().__new__(cls)
        # Добавление названия дома в историю
        if args:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name: str, of_floors: int):
        # Инициализация атрибутов объекта
        self.name = name
        self.of_floors = of_floors

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, target_floor: int):
        # Проверка, что target_floor является целым числом
        if not isinstance(target_floor, int):
            print("Ошибка: target_floor должен быть целым числом")
            return
        if 1 <= target_floor <= self.of_floors: # Проверка, существует ли такой этаж
            for n in range(1, target_floor + 1):
                print(n, self.name)
        else:
            print(f'"Такого этажа не существует" {self.name} всего этажей: {self.of_floors}')

    def __len__(self):
        return self.of_floors

    def __str__(self):
        string_out = f'"Название: {self.name}, кол-во этажей: {self.of_floors}"'
        return string_out

    # Методы для перегрузки операторов сравнения
    def __eq__(self, other):
        if isinstance(other, House):
            return self.of_floors == other.of_floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.of_floors < other.of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.of_floors <= other.of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.of_floors > other.of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.of_floors >= other.of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.of_floors != other.of_floors
        return NotImplemented

    # Методы для перегрузки операторов сложения
    def __add__(self, value):
        if isinstance(value, int):
            self.of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        raise TypeError("Можно добавлять только числа")

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        raise TypeError("Можно добавлять только числа")

#########################################################################################
# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем последний объект
del h1  # ЖК Эльбрус снесён, но он останется в истории


