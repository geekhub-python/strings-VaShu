#!/usr/bin/env python

# задание 8

"""
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите.

*Задача должна быть решена без использования циклов*
"""

# stroka1 = 'skfjh dcsh cdhd chdhch hhhc dhdqw'
# stroka2 = 'fskfjh dcsh cdhd chdhch hhfhc dhqw'
# stroka3 = 'skфaeh dcuy cdhd chdhch hhhc dhdqw'

stroka = input('input : ')
if stroka.count('f') == 1:
    print('Символ один, индекс = ', stroka.find('f'))
elif stroka.count('f') >= 2:
    print('Символов >= 2, индекс1 = ', stroka.find('f'), ', индекс2 = ', stroka.rfind('f'))
else:
    pass
# print('Символа f нет, ничего не делаем')

# второй вариант
#
# if stroka.find('f') == -1:
#     pass
# elif stroka.find('f') == stroka.rfind('f'):
#     print(stroka.find('f'))
# else:
#     print(s.find('f'), s.rfind('f'))
#
