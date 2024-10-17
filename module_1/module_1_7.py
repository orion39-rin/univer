#Задание "Средний балл":
#Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать
# вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#На вход даны следующие данные:

#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

#Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

#Вывод в консоль:
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

#Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sorted = sorted(list(students)) # создаем сортированный список
                                         # учеников. ПОЧЕМУ-ТО МЕТОД .SORT() НЕ СРАБОТАЛ???!!!
average_score = []                       # объявляем список среднего балла
journal = {}                             # объявляем словарь для пар ученик:средний балл

# average_score.append(sum(grades[0])/len(grades[0]))
# average_score.append(sum(grades[1])/len(grades[1]))
# average_score.append(sum(grades[2])/len(grades[2]))
# average_score.append(sum(grades[3])/len(grades[3]))
# average_score.append(sum(grades[4])/len(grades[4]))

#НУ ЕГО НА НА ФИГ - ВРУЧНУЮ ДОЛГО, НАШЕЛ НОВЫЙ МЕТОД ДЛЯ СПИСКА. ЭВРИКА!!!
# !!!!!полезная ссылка (skillbox.ru/media/code/spiski-v-python-chto-eto-takoe-i-kak-s-nimi-rabotat/)

for i in grades:
    x_sum = sum(i)/len(i)                           # вычисляем средний балл E оценок деленная на их число
    #average_score.append(sum(i)/len(i))
    average_score.append(x_sum)                     # записываем средний балл в таблицу оценок
    x_index = len(average_score)-1                  # "КОСТЫЛЬ" - не знаю как правильно синхронизировать
                                                    # индекс списка учеников с итерациями цикла , еще и
                                                    # индекс начинается с нуля...
                                                    # Получилась синхронизация так себе....
    journal.update({students_sorted[x_index] : x_sum})

print(journal.items())