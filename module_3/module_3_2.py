# Домашняя работа по уроку "Способы вызова функции"

# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя
# (администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно
# именованный аргумент со значением по умолчанию - отправитель.
#
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на
# экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено
# с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на
# адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
#
#
# Пример результата выполнения программы:
# Пример выполняемого кода (тесты):
#
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
#
# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!
#
# Примечания:
# Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
# Именованные аргументы всегда идут после позиционных.

def check_email_address(email, domains=['.com', '.ru', '.net']):
    if not '@' in email:
        check_1 = False
        return check_1
    for domain in domains:
        if email[-len(domain):] == domain:
            check_1 = True
            return check_1
        else:
            check_1 = False
    return check_1


def send_email(message, recipient, sender = "university.help@gmail.com"):
    if not check_email_address(recipient) or not check_email_address(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        send_check = False
        return send_check
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        send_check = False
        return send_check
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    send_check = True
    return send_check

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


# sender = "university.help@gmail.com"
# domain = '.com'
# print(sender[-len(domain):])