# Домашнее задание по уроку "Специальные методы классов"
"""Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать атрибут
этажности self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять
атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашнему заданию

Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример результата выполнения программы:

Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20

10
20
"""

class House:
    def __init__(self):
        self.numberOfFloors = 0   # Инициализируем атрибут этажности

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors    # Изменяем значение этажности
        print(self.numberOfFloors) # Выводим новое значение в консоль
        #return self.numberOfFloors

# Пример использования
house = House()               # Создаём экземпляр класса House
house.setNewNumberOfFloors(3) # Изменяем этажность на 3
house.setNewNumberOfFloors(5) # Изменяем этажность на 5

##########################################################################################################

class House_new:
    def __init__(self, name: str, of_floors: int):
        # Инициализация атрибутов объекта
        self.name = name
        self.of_floors = of_floors

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



# Пример использования

h1 = House_new('ЖК Эльбрус', 10)
h2 = House_new('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))