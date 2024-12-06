# Домашнее задание по теме "Файлы в операционной системе"
"""Ваша задача: Освоить работу с файловой системой в Python, используя модуль os.
Цель задания: Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
и использование модуля time для корректного отображения времени."""
'''
Задание:
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:
Ключевая идея – использование вложенного for
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')

Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в 
папке проекта (directory = “.”)
Пример возможного вывода:
Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, 
Родительская директория.'''
##############################################################################################################

import os
import time

# Указываем директорию для поиска
directory = "."  # Текущая директория

# Обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Полный путь к файлу
        filepath = os.path.join(root, file)

        # Время последнего изменения файла в формате timestamp
        filetime = os.path.getmtime(filepath)

        # Преобразуем время в читаемый формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Родительская директория
        parent_dir = os.path.dirname(filepath)
#изменим задачу и будeм выводить информацию о файлах с расширениями txt и log
        # Вывод информации о файле
        if file.lower().endswith((".log",".txt")): # кортеж расширений
            print(
                f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, "
                f"Время изменения: {formatted_time}, Родительская директория: {parent_dir}"
            )
