# Домашнее задание по теме "Режимы открытия файлов"
"""Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами."""
'''Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать
 следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены 
запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую 
строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в 
файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, 
то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.'''
"""
Пример результата выполнения программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato уже есть в магазине
Продукт Spaghetti уже есть в магазине
Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Примечания:
Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
Не забывайте закрывать файл вызывая метод close() у объектов файла."""
############################################################################################################

class Product:
    """
    Класс для описания продукта.
    :param name: Название продукта (строка).
    :param weight: Общий вес продукта (дробное число).
    :param category: Категория продукта (строка).
    Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'
    """

    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # Атрибут name - название продукта (строка).
        self.weight = weight # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category # Атрибут category - категория товара (строка).

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """
        Считывает все продукты из файла и возвращает их как единую строку.
        Если файл не существует или пуст, возвращает пустую строку.
        WITH - АВТОМАТИЧЕСКИ закрывает файл при любом сценарии
        """

        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            # Если файл не существует, возвращаем пустую строку
            return ""


    def add(self, *products):
        """
        Добавляет продукты в файл, если их там ещё нет.
        :param products: Объекты класса Product.
        """
        # Считываем текущие продукты из файла
        existing_products = self.get_products()
        # Генерируем множество названий продуктов в магазине - убираются дубликаты, быстрее поиск чем в строке
        existing_names = {line.split(', ')[0] for line in existing_products.splitlines()}

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_names:
                    # Если продукт уже существует, выводим сообщение
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    # Если продукта нет, добавляем его в файл
                    file.write(str(product) + '\n')
                    print(f"Продукт {product.name} добавлен в магазин")

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())




