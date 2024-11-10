# Домашнее задание по уроку "Пространство имен"

# Создайте новый проект в PyCharm
# Запустите созданный проект

# Ваша задача:
#
# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать
# значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# Файл с кодом module_4_2.py загрузите на GitHub репозиторий и пришлите ссылку на него.


str_global = 'Я в глобальной области видимости'

def test_function():
    """
    Пространства имен и области видимости
    """
    str_1 = "Я в области видимости функции test_function"

    def inner_function(str_inner):
        print(f'\n ______________start inner_function___________')
        print(locals())
        print(locals().get('str_1', 'в локальной области inner_function  нет str_1'))
        print(locals().get("str_inner", 'в локальной области inner_function  нет str_inner'))
        print('______________end inner_function___________')

    inner_function('TeSt для переменной str_inner')

    print(f'\n ----------------блок test_function после вызова inner_function --------')
    print(str_1)
    print(locals())
    print(locals().get("str_inner", 'в локальной области test_function  нет str_inner'))
    print(globals().get('str_global'))
    print(f'-------------- конец test_function ------------------ \n')

test_function()
help(test_function)
# так нагляднее (для маленькой диагонали дисплея)
# плюс интересный костыль "use list to force a copy of the keys", без list был абзац)))
for z in list(globals().items()):
    print(z)