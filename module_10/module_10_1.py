#Домашнее задание по теме "Создание потоков"
"""Задача "Потоковая запись в файлы":"""

'''Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
 file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием 
после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:

10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:

10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.

Также измерьте время затраченное на выполнение функций и потоков. 
Как это сделать рассказано в лекции к домашнему заданию.

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

Вывод на консоль:

Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время

Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время

Записанные данные в файл должны выглядеть так:

Примечания:
Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках 
не должно превышать ~20 секунд, а в функциях ~34 секунды.
Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали 
почти одновременно.'''
####################################################################################################################
import threading
import time
from threading import current_thread


# def time_run(func, *args, **kwargs):
#     t_start = time.time()
#
#     result = func(*args, **kwargs)
#
#     t_end = time.time()
#     t_run = round(t_end - t_start, 4)
#     print(f'Функция {func.__name__}  работала {t_run} секунд(ы)')
#     return result

def time_run(func):
    def wrapper(*args, **kwargs):
        t_start = time.time()

        result = func(*args, **kwargs)

        t_end = time.time()
        t_run = round(t_end - t_start, 4)
        if func.__name__ == 'write_words':
            # Попытка извлечь 'file_name' из kwargs
            #file_name = kwargs.get('file_name', 'неизвестно')
            file_name = args[1] if len(args) > 1 else 'неизвестно'
            word_count = args[0] if len(args) > 1 else 'неизвестно'
            print('---------------------------------------------')
            print(f'Функция {func.__name__}  с аргументами: word_count = {word_count} {file_name} '
                  f'работала {t_run} секунд(ы)')
        else:
            print('++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Функция {func.__name__} работала {t_run} секунд(ы) !!!!! \n  ')
        return result
    return wrapper

@time_run
def write_words(word_count=8, file_name='example1.txt'):
    #word = input('введите слово: ')
    word = 'Nika'

    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(1, word_count+1):
            time.sleep(0.1)
            file.write(f'{word}  №{i} \n' )

    print(f'Завершилась запись в файл {file_name}')


# Вызов функции write_words с разными параметрами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')


# Список параметров
params = [
    (10, 'example1.txt'),
    (30, 'example2.txt'),
    (200, 'example3.txt'),
    (100, 'example4.txt'),
]

# Цикл для вызова функции с каждым набором параметров
# for word_count, file_name in params:
#     write_words(word_count, file_name)

# Вспомогательная функция для вызова write_words с разными параметрами
def call_write_words(params_list):
    for word_count, file_name in params_list:
        write_words(word_count, file_name)

# Вызов вспомогательной функции
call_write_words(params)

"""ИНТЕРЕСНО будет ли при таком вызове в декораторе доступ к ссылке на params? если да - то есть риск (или возможность)
 изменения списка. это нарушение безопасности по идее. вроде есть запрет передачи изменяемых параметров. тогда надо
разобраться с возможностью передачи списка внутри кортежа. 
или вообще предварительно создавать буферную переменную-кортеж.....
считаю, что это надо исследовать. 
но блин, чем дальше в лес (влез), тем толще партизаны((( уже в черепушке все не умещается"""

#а ща замахнемся на вильяма нашего - шекспира!!!

# Вспомогательная функция для вызова write_words с разными параметрами с декоратором тайминга и ДВОЙНЫМ ВЫЗОВОМ
#декоратора почти РЕКУРСИЯ - что будет с пространством данных????
@time_run
def call_write_words_decor(params_list):
    for word_count, file_name in params_list:
        write_words(word_count, file_name)

call_write_words_decor(params)
# Ура! вроде фунциклирует!!!! надо с жуком интимом заняться основательно)

#############################################################################################
#теперь ПОТОКИ
#СТАНДАРТНЫЙ вариант
# Измерение времени выполнения потоков
start_time_threads = time.time()

# Создание потоков отдельно
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

# Запуск потоков
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Ожидание завершения всех потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_threads = time.time()
print('========================================================================================')
print(f'Работа потоков {end_time_threads - start_time_threads} !!!! \n')


# немного АВТОМАТИЗАЦИИ))))
# Измерение времени выполнения потоков
start_time_threads = time.time()

# Создание потоков
threads = []
params = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for word_count, file_name in params:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print('============================================================================')
print(f'Работа потоков {end_time_threads - start_time_threads} !!!! \n')

print(f' ВЫВОДы: \n 1. потоки ЗНАЧИТЕЛЬНО сокращают время выполнения программы! '
      f'(очень полезная хрень, если железо норм)\n 2. метод вызова потока или функции практически НЕ влияет на '
      f'время выполнения\n хотя надо покопать глубже \n 3. надо разбираться с пространством данных при использовании'
      f' декоратора\n особенно одного одновременно с несколькими функциями\n при этом особое внимание передаче'
      f' в аргументы декорируемой функции списка ')
