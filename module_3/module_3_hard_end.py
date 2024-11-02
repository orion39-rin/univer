# Дополнительное практическое задание по модулю: "Подробнее о функциях."

# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами
# путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее,
# даже после сна, его код остался рабочим и выглядел следующим образом:

# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин
# всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких
# структур он не нашёл.
# Помогите сокурснику осуществить его задумку.

# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
#
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# result = calculate_structure_sum(data_structure)
# print(result)

# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
"""
Завтра днюха, точнее уже сегодня...

Еще месяц назад не знал слова PyCharm...

Решил приколоться и записать свои мысли в молодежном стиле - хочу сына заинтересовать программированием.
Может к кодингу интерес проявит. Показал ему с гордостью exeшник убогого калькулятора, который весит
почти 10 метров (кодеры на асме и си сожгли бы меня на перфокартах, причем, раза три - для надежности))).

И так - Хэллоуин в самом разгаре)))

Записки охотника. (для кого ассоциируется Тургеньев, а для кого 'на вампиров', вторым и посвящается...)

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Вопрос раз - нужно ли считать сумму индексов строки или списка?
Т.к. len('astra') = 5 еще имеет сумму индексов sum_index = 0+1+2+3+4 (есть еще количество элементов, ключей,
числовое значение символа ......).
Буду считать, что НЕТ, хотя надо бы решить и этот вариант))
Это немного упрощает житуху).

Что считаем (подозреваю, что ЭТО будет определением КОНЕЧНОГО условия рекурсии):
1. если int, тогда суммируем...
2. если str, тогда len() и опять смотри пункт 1 (напоминает про устав и командира...).

Где каким методом достаем эти intы и strы (определимся с типами данных и методами)
список lict - index, len, range, for in []
кортеж tuple - index, len, range, for in ()
словарь dict - key:value, for key, value in {}.items()
Для проверки типа данных - функция type или isinstance (читал где-то, что,
в отличии, от type учитывает наследие типа)
ОСНОВНАЯ задача - достать все элементы из входного зоопарка с матрешками, а дальше дело техники!!!!

Теперь мозговать надо над функциями обработки каждого типа и что применять рекурсию(ненавижу) или итерацию.
А лучше оба варианта... (для сравнения и надо учиться готовить кошек, чтобы нравились))

pass мне в помощь...

Туби or not туби?? вопрос два раза:

if type(element) == int:
    pass
OR--------
if isinstance(element, int):
    pass

Рекурсия OR Итерация - КАК проще перебрать все элементы???

придется сравнить...
поехали...
"""
##############################################################################################
import time

def sum_list_element(elements):
    sum_elements = 0
    temp_elements = []

    for element in elements:
        if type(element) == int:
            sum_elements += element
        elif type(element) == str:
            sum_elements += len(element)
            # for letter in element:
            #     if letter.isdigit():
            #         sum_elements += int(letter)
        else:
            if type(element) == dict:
                # Просто распакую словарь и закину все элементы во временный список
                # для обработки на следующей итерации.
                for key, value in element.items():
                    temp_elements.extend([key, value])
            else:
                for z in element:
                    temp_elements.append(z)
    return temp_elements, sum_elements


def calculate_structure_sum(elements):
    start = time.perf_counter()
    sum_elements = 0
    temp_elements = []
    trigger = True  #На всякий пожарный запускаю while через True, можно None, чтобы проще
    # выключить его, ибо здесь в условии мы точно не сможем использовать счетчик. А запускать его в
    # бесконечном цикле вообще не кашерно.
    while trigger == True:

        for element in elements:

            if type(element) == int:
                sum_elements += element

            elif type(element) == str:
                sum_elements += len(element)
                for letter in element:
                    if letter.isdigit():
                        sum_elements += int(letter)

            elif type(element) == list:
                add_element, add_sum = sum_list_element(element)
                if len(add_element) > 0:
                    temp_elements.append(add_element)
                sum_elements += add_sum

            elif type(element) == tuple:
                element = list(element)
                add_element, add_sum = sum_list_element(element)
                if len(add_element) > 0:
                    temp_elements.append(add_element)
                sum_elements += add_sum

            elif type(element) == dict:
                # Просто распакую словарь и закину все элементы во временный список
                # для обработки на следующей итерации.
                for key, value in element.items():
                    temp_elements.extend([key, value])
                # Интересно, а можно проще???
                # temp_elements.extend(element.items())
                # АРБАЙТЕН!!!!! но ХУЖЕ - возвращает кортежи ключ:значение - это увеличит число итераций((((
            # else:
            #     pass
        if len(temp_elements) == 0:
            finish = time.perf_counter()
            print('Время работы в секундах КОСТЫЛИ: ' + str(finish - start))
            return sum_elements # Обошелся без переключения True для выхода из while.
        else:
            # разделим адресные пространства переменных elements (её будем заново передавать
            # в новую итерацию на обработку) и temp_elements(в которой хранятся не обработанные
            # в этой итерации элементы) ИБО при простом присвоении = получается БЕДА)))
            elements = []
            for x in temp_elements:
                elements.append(x)
            # Соответственно, обнуляем временное хранилище для промежуточных результатов.
            temp_elements = []
            # Запускаем по новой. Улыбаемся и машем)))

########################################################################################################
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
"""
Это просто абзац какой-то... Я практически всю ночь в интимных отношениях с отладчиком)))
НО ПРАВИЛЬНЫЙ ОТВЕТ НЕ 99 А....101
Считаем:
красивый ряд 1 - 8, 2, Urban2 = 2, 35 == 75
суммируем длины строк 1, 1, 4, 4, 5, 5, 6 == 26
ИТОГО: 101.......

Это не Записки охотника, а скорее Как закалялась сталь (к сожалению, не про самураев)))
Зато, появилось устойчивое убеждение, что надо учиться готовить кошек, то есть, начинать любить РЕКУРСИЮ)))
Но это чуть позже... Отладчик напрочь отбил любилку. 
Неужели я такой тупенький - столько времени на простую задачу? Столько костылей в коде, что наверное 
надо идти работать в травматологию...
"""
###########################################################################################################
result = calculate_structure_sum(data_structure)
print('Результат выполнения функции КОСТЫЛИ: ', result, '\n')

############################################################################################################
#
"""
Представляю вашему вниманию модернизированный вариант кода ИТЕРАТИВНОГО варианта решения задачи без модуля
 обработки чисел в строках.
Первоначальный вариант был нацелен на быстродействие и страдал огромным количеством костылей.
Попробую вычислить время выполнения кода Костыли vs Дзен.
# подключаем модуль time
import time
# фиксируем время старта работы кода
start = time.process_time()

# код, время работы которого измеряем

#фиксируем время окончания работы кода
finish = time.process_time()
# вычитаем время старта из времени окончания и выводим результат
print('Время работы: ' + str(finish - start)) 
"""
############################################################################################################

def calculate_structure_sum_iteration(elements):
    start = time.perf_counter()
    sum_elements = 0
    temp_elements = []
    trigger = True  #На всякий пожарный запускаю while через True, можно None, чтобы проще
    # выключить его, ибо здесь в условии мы точно не сможем использовать счетчик. А запускать его в
    # бесконечном цикле без возможности отключения вообще не кашерно.
    while trigger == True:

        for element in elements:
            if type(element) == int:
                sum_elements += element
            elif type(element) == str:
                sum_elements += len(element)
            elif type(element) == dict:
                for key, value in element.items():
                    temp_elements.extend([key, value])
            else:
                for atom in element:
                    temp_elements.append(atom)

        if len(temp_elements) == 0:
            finish = time.perf_counter()
            print('Время работы в секундах ДЗЕН: ' + str(finish - start))
            return sum_elements # Обошелся без переключения True для выхода из while.
        else:
            # разделим адресные пространства переменных elements (её будем заново передавать
            # в новую итерацию на обработку) и temp_elements(в которой хранятся не обработанные
            # в этой итерации элементы) ИБО при простом присвоении = получается БЕДА)))
            elements = []
            for x_atom in temp_elements:
                elements.append(x_atom)
            # Соответственно, обнуляем временное хранилище для промежуточных результатов.
            temp_elements = []
            # Запускаем по новой. Улыбаемся и машем)))

###############################################################################################
result_iteration = calculate_structure_sum_iteration(data_structure)
print('Результат выполнения усовершенствованной ИТЕРАТИВНОЙ функции ДЗЕН: ', result_iteration, '\n')

###########################################################################################

count_number_of_recursion_calls = 0 # Счетчик вызовов рекурсии в глобальном адресном поле

def calculate_structure_sum_recursion(elements):
    global count_number_of_recursion_calls
    start_recursion = time.perf_counter()
    sum_elements = 0
    temp_elements = []

    for element in elements:
        if type(element) == int:
            sum_elements += element
        elif type(element) == str:
            sum_elements += len(element)
        elif type(element) == dict:
            for key, value in element.items():
                temp_elements.extend([key, value])
        else:
            for atom in element:
                temp_elements.append(atom)
    if len(temp_elements) == 0:
        return sum_elements # КОНЕЧНОЕ УСЛОВИЕ РЕКУРСИИ!!!! ОБРАБОТАНЫ ВСЕ ЭЛЕМЕНТЫ ВСЕХ СЛОВАРЕЙ И МНОЖЕСТВ.
    else:
        result = sum_elements + calculate_structure_sum_recursion(temp_elements)
        count_number_of_recursion_calls += 1
        finish_recursion = time.perf_counter()
        print(f'вызов рекурсии № {count_number_of_recursion_calls} Время работы в секундах #$%^%$кошки:  '
              + str(finish_recursion - start_recursion))
        return result

##################################################################################################
result_recursion = calculate_structure_sum_recursion(data_structure)
print('Результат выполнения РЕКУРСИВНОЙ функции #$%^%$кошки: ', result_recursion, '\n')
print('ИТЕРАТИВНЫЙ код проще, легче в отладке и, в данном случае, на порядок быстрее РЕКУРСИВНОГО!!!!')
##################################################################################################
"""
Пальцы зажили.
Буря эмоций улеглась.
Немного изучил рецепты приготовления кошатины...
В заключение. (не по этапу, конечно, а итог для себя...)
--КОСТЫЛИ это моё ОШИБОЧНОЕ мнение, что уменьшение количества ИТЕРАЦИЙ в ущерб простоте КОДА может ускорить 
выполнение программы.
--Линейный простой код ЛУЧШЕ И БЫСТРЕЕ (в данном случае на порядок) любой итерации, может конечно потребовать
костыль, НО гораздо проще в отладке и , лично для меня, проще в понимании. 
Несмотря на то, что понимаю принцип работы СТЕКА и основы построения рекурсий, не импонируют мне кошки. 
Я обожаю ротвейлеров).
Короче ДЗЕН рулит!
Если кто- то дочитал эту ахинею, пришлите мне пожалуйста ссылку на нормальное решение этой ЗАДАЧИ
 рекурсивным методом для сравнения и изучения.
"""