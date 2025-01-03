# Домашнее задание по теме "Позиционирование в файле"
# Задача "Записать и запомнить":
"""
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью."""
'''
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.'''
'''
Пример результата выполнения программы:
Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')

Примечания:
Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
Не забывайте закрывать файл вызывая метод close() у объектов файла.
Помните, что при использовании символов не принадлежащих таблице ASCII, вы используете больше байт для записи 
символа. Соответственно для чтения и записи информации из/в файл(-f) потребуется другая кодировка - utf-8.'''
###############################################################################################################

def custom_write(file_name, strings):
    """
    Записывает строки в файл, возвращает словарь с позициями начала строк и их содержимым.
    :param file_name: Имя файла для записи.
    :param strings: Список строк для записи.
    :return: Словарь, где ключ - кортеж (номер строки, байт начала строки), значение - строка.
    """
    # Словарь для хранения информации о позициях строк
    strings_positions = {}

    # Открываем файл для записи с указанием кодировки utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, line in enumerate(strings, start=1):  # Перебираем строки с номерами, начиная с 1
            position = file.tell()  # Получаем текущую позицию указателя в байтах
            file.write(line + '\n')  # Записываем строку в файл с символом переноса строки
            strings_positions[(line_number, position)] = line  # Сохраняем данные в словарь

    return strings_positions  # Возвращаем итоговый словарь

# ##############
# можно использовать классическую конструкцию
# # Открываем файл в режиме записи с указанием кодировки utf-8
# file = open(file_name, 'w', encoding='utf-8')
# try:
#     for line_number, line in enumerate(strings, start=1):  # Перебираем строки с номерами
#         position = file.tell()  # Получаем текущую позицию указателя в байтах
#         file.write(line + '\n')  # Записываем строку с символом переноса строки
#         strings_positions[(line_number, position)] = line  # Добавляем запись в словарь
# finally: #!!!!Блок finally гарантирует, что файл будет закрыт, даже если внутри блока try произошла ошибка.
#     file.close()  # Закрываем файл вручную
#
# return strings_positions  # Возвращаем словарь
# ############

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


