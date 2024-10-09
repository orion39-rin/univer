# методы TITLE UPPER LOWERS
from tkinter.font import names

name = "ada lovelace ADA adA AdA"
print(name)
print(name .title())
print(name .upper())
print(name .lower())

print()

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

#тоже самое, но с использованием переменной
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

print()

# включения в текст позиции табуляции используется комбинация символов \t,
# как в точке :
print("Python")
print("\tPython")
# Разрывы строк добавляются с помощью комбинации символов \n:
print("Languages: Python C JavaScript")
print("Languages:\nPython\nC\nJavaScript")

# Табуляции и разрывы строк могут сочетаться в тексте. Скажем, последовательность
# "\n\t" приказывает Python начать текст с новой строки, в начале которой
# располагается табуляция.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Удаление пропусков

# Значение, хранящееся в переменной favorite_language, содержит # лишние пропуски в конце строки.
#Когда метод rstrip() работает с переменной favorite_language этот лишний пробел удаляется.
# Впрочем, удаление лишь временное: если снова запросить значение
# favorite_language, мы видим, что строка не отличается от исходной, включая лишний пропуск.
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

# Чтобы навсегда исключить пропуск из строки, следует записать усеченное значение обратно в переменную:
favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip() # преобразуем переменную удаляя лишние пробелы
print(favorite_language)
# Сначала пропуски удаляются в конце строки, а потом значение записывается в исходную переменную.

# Пропуски также можно удалить у левого края (в начале) строки при помощи метода
# lstrip(), а метод strip() удаляет пропуски с обоих концов:
favorite_language = '      python     '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

 # Личное сообщение: сохраните имя пользователя в переменной и выведите
 # сообщение, предназначенное для конкретного человека. Сообщение должно быть
 # простым, например: “Hello Eric, would you like to learn some Python today?”

name = input('Введите Ваше имя: ') .title() .strip()
#name = name + ','
print('Hello', name + ',', 'would you like to learn some Python today?')

# Знаменитая цитата: Выведите текст цитаты с именем автора. Результат должен выглядеть
# примерно так (включая кавычки): Albert Einstein once said, "A person who never made a mistake
# never tried anything new."
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# Знаменитая цитата 2: повторите упражнение, но на этот раз сохраните имя автора
# цитаты в переменной famous_person. Затем составьте сообщение и сохраните его в новой
# переменной с именем message. Выведите свое сообщение.
famous_person = 'Albert Einstein'
message = '"A person who never made a mistake never tried anything new."'
print(famous_person, 'once said,', message)

# Удаление пропусков: сохраните имя пользователя в переменной. Добавьте в начале и
# в конце имени несколько пропусков. Проследите за тем, чтобы каждая служебная
# последовательность , “\t” и “\n”, встречалась по крайней мере один раз.
# Выведите имя, чтобы были видны пропуски в начале и конце строки. Затем выведите его
# снова с использованием каждой из функций удаления пропусков: lstrip(), rstrip() и strip().
name = '   Serg   '
name1 = '         Orion         '
name2 = '         NIKA     '
print('Выводим исходные значения переменных')
print('\t', name, '\n\t', name1, '\n\t', name2)
print('Знаками * отображаем границы пробелов по краям имен')
print('\t', '*' + name + '*', '\n\t', '*' + name1 + '*', '\n\t', '*' + name2 + '*')
print('Используем функции удаления пропусков: lstrip(), rstrip() и strip()')
print('\t', '*' + name.lstrip() + '*', '\n\t', '*' + name1.rstrip() + '*', '\n\t', '*' + name2.strip() + '*')

# Число 8: напишите операции сложения, вычитания, умножения и деления, результатом которых
# является число 8. Не забудьте заключить операции в команды print, чтобы проверить результат.
print('5 + 3 =', 5 + 3)
print('39 - 31.0 =', 39 - 31.0)
print('4 * 2 =', 4 * 2)
print('16.0 / 2 =', 16.0 / 2)

# Любимое число: сохраните свое любимое число в переменной. Затем при помощи
# переменной создайте сообщение для вывода этого числа. Выведите это сообщение.
number = 39.0
print('Лучшее число ' + str(number) + ', а не 42!!!')
print('Лучшее число ' + str(int(number)) + ', а не 42!!!')

#СПИСКИ
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
#Индексы начинаются с 0, а не с 1
#Второму элементу списка соответствует индекс 1.
#В этой простой схеме индекс любого элемента вычисляется уменьшением на 1 его позиции в списке.
# Например, чтобы обратиться к четвертому элементу списка, следует запросить элемент с индексом 3.
print('Вывод третьего элемента:', bicycles[2])

#специальный синтаксис для обращения к последнему элементу списка.
#Если запросить элемент с индексом –1, Python всегда возвращает последний элемент в списке:
#Индекс –2 возвращает второй элемент от конца списка, индекс –3 — третий элемент от конца и т.д.
print('Вывод последнего элемента:', bicycles[-1])

names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names)
print('Сейчас я изучаю', names[0])
print('хочу еще изучить', names[1-5], names[2], names[-2].upper(), names[-1])

# Изменение элементов в списке
# Синтаксис изменения элемента напоминает синтаксис обращения к элементу списка.
# Чтобы изменить элемент, укажите имя списка и индекс изменяемого элемента в
# квадратных скобках; далее задайте новое значение, которое должно быть присвоено элементу.
names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names) 
names[-1] = 39
print(names)
print(type(names[-1]))

# Добавление элементов в список

#Присоединение элементов в конец списка
names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names)
names.append(39)     #Присоединение элементов в конец списка
names.append('регион')
print(names)

names = []         #объявление пустого списка
print(names)
names.append(39)
print(names)
names.append('регион')
print(names)

#Вставка элементов в список
#Метод insert() позволяет добавить новый элемент в произвольную позицию списка.
#Для этого следует указать индекс и значение нового элемента.
names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names)
names.insert(3,'C#')
print(names)

# Удаление элементов из списка
names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names)
del names[-1]         # удаление по номеру позиции
print(names)

# Метод pop() удаляет элемент из списка, но позволяет работать с ним после удаления.
names = ['Python', 'C', 'C++', 'Assembler', 'java'] 
print(names)                                        
popped_names = names.pop(2)
print(names)
print(popped_names)

#Удаление элементов по значению
names = ['Python', 'C', 'C++', 'Assembler', 'java']
print(names)
names.remove('Assembler')
print(names)
element_for_del = 'java'
names.remove(element_for_del)
print(names)
print('был удален элемент:', element_for_del)





















































