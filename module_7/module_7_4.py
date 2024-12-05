#Домашнее задание по теме "Форматирование строк"
"""История: соперничество двух команд - Мастера кода и Волшебники данных.
Задание:
Использование %:
Переменные: количество участников первой команды (team1_num).
Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
Переменные: количество участников в обеих командах (team1_num, team2_num).
Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

Использование format():
Переменные: количество задач решённых командой 2 (score_2).
Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
Переменные: время за которое команда 2 решила задачи (team1_time).
Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"

Использование f-строк:
Переменные: количество решённых задач по командам: score_1, score_2
Пример итоговой строки: "Команды решили 40 и 42 задач.”
Переменные: исход соревнования (challenge_result).
Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."

Комментарии к заданию:
В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.
Например, для challenge_result:
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
result = ‘Победа команды Мастера кода!’
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
result = ‘Победа команды Волшебники Данных!’
else:
result = ‘Ничья!’

Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
"""
####################################################################################################

#Использование %:
team1 = "Мастера кода"
team2 = "Волшебники Данных"
team1_num = 5
team2_num = 6
string_team1 = "В команде %s участников: %s !" %(team1, team1_num)
string_team2 = "В команде %s участников: %s !" %(team2, team2_num)
string_team_all = "Итого сегодня в командах участников: %(t1)s и %(t2)s !" %{'t1': team1_num, 't2': team2_num}

# Использование format():
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
string_team1_score = "Команда {} решила задач: {} !".format(team1, score_1)
string_team1_time = "{} решили задачи за {} с !".format(team1, team1_time)
string_team2_score = "Команда {name} решила задач: {score} !".format(name=team2, score=score_2)
string_team2_time = "{name} решили задачи за {time} с !".format(name=team2, time=team2_time)

# Использование f-строк:
string_score_all = f'Команды решили {score_1} и {score_2} задач.'
string_time_avg = (f"Сегодня было решено {score_1 + score_2} задач, в среднем "
                   f"по {round((team1_time + team2_time) / (score_1 + score_2), 2)} секунды на задачу!.")

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

string_challenge_result = f"Результат битвы: {result}"

if __name__ == '__main__':
    print(string_team1)
    print(string_team2)
    print(string_team_all)
    print(string_team1_score)
    print(string_team1_time)
    print(string_team2_score)
    print(string_team2_time)
    print(string_score_all)
    print(string_time_avg)
    print(string_challenge_result)
