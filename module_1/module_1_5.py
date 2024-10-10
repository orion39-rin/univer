#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

#Цель: Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми
# и изменяемыми объектами.

# Задайте переменные разных типов данных:
# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.

#3. Изменение значений переменных:
#  - Попытайтесь изменить элементы кортежа immutable_var. Объясните,
#  почему нельзя изменить значения элементов кортежа.

#4. Создание изменяемых структур данных:
#- Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#- Измените элементы списка mutable_list.
#- Выведите на экран измененный список mutable_list.
#
# Пример результата выполнения программы:
# Immutable tuple: (1, 2, 'a', 'b')
# Mutable list: [1, 2, 'a', 'b', 'Modified']

mutable_list = [1, 3.14, 'region', True, [100, 200, 300]] # список
print('список mutable_list =', mutable_list, type(mutable_list), mutable_list.__sizeof__(), 'bytes')

#immutable_var = tuple([1, 3.14, 'region', True, [100, 200, 300]])

immutable_var = tuple(mutable_list)                        # кортеж (преобразование списка в кортеж)
print('кортеж immutable_var =', immutable_var, type(immutable_var), immutable_var.__sizeof__(), 'bytes')

# В кортеже возможно изменять значения изменяемых элементов

immutable_var[4][0] = 39 #Изменяем первый элемент списка, являющегося пятым элементом кортежа
print(immutable_var)
immutable_var[4][1] = 'True'
print(immutable_var)
immutable_var[4][2] = True
print(immutable_var)
immutable_var[4].insert(2, 'V') # делаем вставку нового элемента списка
print(immutable_var)
del immutable_var[4][2]                        # удаляем этот элемент
print(immutable_var)
del immutable_var[4][1:3]
print(immutable_var)

immutable_var = (1, 'два', 3.14)
print('кортеж immutable_var =', immutable_var, type(immutable_var), immutable_var.__sizeof__(), 'bytes')
immutable_var = immutable_var * 3 #операция умножения кортежа
print('кортеж immutable_var =', immutable_var, type(immutable_var), immutable_var.__sizeof__(), 'bytes')

immutable_var = (1,) + ('два', 3.14) #  конкатенация кортежей
print('кортеж immutable_var =', immutable_var, type(immutable_var), immutable_var.__sizeof__(), 'bytes')
