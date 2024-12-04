'''Создайте новый проект или продолжите работу в текущем проекте
Ваша задача:
Создайте в директории проекта текстовый файл с расширением txt
Добавьте в этот файл следующий текст
# -*- coding: utf-8 -*-

Создайте переменную с этим файлом
Распечатайте содержимое текстового файла в консоль
Закройте файл
Получившийся код прикрепите к заданию текстом'''
name = 'm_7_1a.txt'
file = open(name, 'w') # r, w, a read write append
file.write("# -*- coding: utf-8 -*-")
file.close()

file = open(name, 'r')
print(file.read())
file.close()

file = open(name, 'a')
file.write('\nMy soul is dark - Oh! quickly string\nThe harp I yet can brook to hear;\n')
file.write("And let thy gentle fingers fling\nIts melting murmurs o'er mine ear.'\n")
file.write("If in this heart a hope be dear,\nThat sound shall charm it forth again:\nIf in these eyes there lurk "
           "a tear,\n'Twill flow, and cease to burn my brain.\nBut bid the strain be wild and deep,\nNor let "
           "thy notes of joy be first:\n")
file.write("I tell thee, minstrel, I must weep,\nOr else this heavy heart will burst;\nFor it hath been by sorrow "
           "nursed,\nAnd ached in sleepless silence, long;\nAnd now 'tis doomed to know the worst,\nAnd break at "
           "once - or yield to song.\n")
file.close()

file = open(name, 'r')
print(file.read())
file.close()