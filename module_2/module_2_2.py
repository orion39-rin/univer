# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"
from itertools import count

# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых
# чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0


# Блок запроса ввода данных и присвоение значений переменным.

# Попробую сделать простейшую проверку корректности ввода числа
# с ограничением числа попыток неправильного ввода

number_input = 3  # Указываем количество попыток ввода числа
first = None   # Задаю первоначальное пустое значение первого и последующих чисел для корректной проверки в цикле
second = None
third = None

print('Введите три числа для сравнения')

# Блок ввода первого числа

count = number_input  # ввожу промежуточный счетчик, чтобы не менять значение заданных попыток ввода
while first is None:                         # Цикл до введения корректного значения
    number_temp = input('Введите первое число: ')  # временная переменная для проверки TRY
    try:  # если следующая операция удалась без ошибки выходи из цикла с введенным числом
        first = float(number_temp)  # использую преобразование FLOAT, числа могут быть и дробными)
    except ValueError: # Обработка ОШИБКИ преобразования FLOAT веденного значения
        count -= 1  # Уменьшаем количество попыток ввода
        print('Введите корректные данные, (не используйте символы)')
        if count == 0:  # Если попыток не осталось выходим из программы
            print('Количество ошибочных вводов превысило', number_input)
            exit()

print('Вы корректно ввели первое число', first)

# Блок ввода второго числа

count = number_input
while second is None:
    number_temp = input('Введите второе число: ')
    try:
        second = float(number_temp)
    except ValueError:
        count -= 1
        print('Введите корректные данные, (не используйте символы)')
        if count == 0:
            print('Количество ошибочных вводов превысило', number_input)
            exit()

print('Вы корректно ввели второе число', second)

# Блок ввода третьего числа

count = number_input
while third is None:
    number_temp = input('Введите третье число: ')
    try:
        third = float(number_temp)
    except ValueError:
        count -= 1
        print('Введите корректные данные, (не используйте символы)')
        if count == 0:
            print('Количество ошибочных вводов превысило', number_input)
            exit()

print('Вы корректно ввели третье число', third)

# Блок обработки введенных чисел на совпадение

print('Теперь посчитаем количество одинаковых чисел')

if first == second and second == third:  # А можно так: if (first + second + third) / 3 == first ????
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

# А если чисел больше трех, то применять списки LIST и метод COUNT
# или LIST + ЦИКЛ + СЛОВАРЬ для пары числа и количества повторений ????

#########################################################################################################
# Помогите пожалуйста разобраться.
#########################################################################################################
#number_input = 3  # Указываем количество попыток ввода числа

#Объявляем функцию с указанием значений параметров по умолчанию (использую NONE для задания первичного
# условия цикла и COUNT, чтобы #не измениять в случае ошибочных вводов значение NUMBER_INPUT)
# def input_number(number_temp = None, count = number_input):
#     while number_temp is None:                         # Цикл до введения корректного значения,
#         number_temp = input('Ввведите число: ')
#         try:
#             number = float(number_temp) # использую преобразование FLOAT, числа могут быть и дробными)
#         except ValueError:
#             count -= 1   # Уменьшаем количество попыток ввода
#             print('Введите корректные данные, (не используйте символы)')
#             if count == 0:   #Если попыток не осталось выходим из программы
#                 print('Количество ошибочных вводов превысило', number_input)
#                 exit()
#     return number   #А вот тут *ОПА!!!!
#
#
# print('Пожалуйста введите три числа для сравнения')
# number_1 = input_number() # Вызываем функцию ввода: если ЧИСЛО - все ОК, если символы - *ОПА!!!!!!!!!!
# print(number_1)
#
# Позже попытаюсь попробовать через isdigit(), но хочется разобраться в этой проблеме.






