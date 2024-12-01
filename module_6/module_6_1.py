# Домашнее задание по теме "Зачем нужно наследование"
"""Цель: применить базовые знания о наследовании классов для решения задачи

Задача "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?

Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное
название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
В данном случае можно использовать принцип наследования, чтобы не дублировать код.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется
атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется
атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

Пункты задачи:

Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.

Пример результата выполнения программы:
Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
Вывод на консоль:
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True

Примечания:
Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
Обращайте внимание на то, где атрибут класса, а где атрибут объекта."""
#######################################################################################################
class Animal:
    alive = True                    # живой/мертвый
    fed = False                     # голодный/накормленный

    def  __init__(self, name):
        self.name = name            #индивидуальное название каждого животного

    def eat(self, food):
        if not isinstance(food, Plant):           #Вводим проверку наследования Plant, для повышения устойчивости кода
            print(f'{self.name} не может есть {food}')
            return
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

    def __repr__(self):
        return f"Animal({self.name}, alive={self.alive}, fed={self.fed})"


class Plant:
    edible = False                  # съедобность/ядовитость

    def  __init__(self, name):      # индивидуальное название каждого растения
        self.name = name

    def __repr__(self):
        return f"Plant({self.name}, edible={self.edible})"


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True  # переопределяем съедобность фруктов

######################################################################################
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1)
print(a1.name)
print(p1)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
print(a1)