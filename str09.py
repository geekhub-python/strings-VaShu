#!/usr/bin/env python

# задание 9

"""
Дана строка. Найдите в этой строке второе вхождение буквы `f`, и выведите индекс этого
вхождения. Если буква `f` в данной строке встречается только один раз, выведите число
`-1`, а если не встречается ни разу, выведите число `-2`.
"""

# stroka1 = 'skfjh dcsh cdhd chdhch hhhc dhdqw'
# stroka2 = '12fskfjh dcsh cdhd chdhch hhfhc dhqw'
# stroka3 = 'skфaeh dcuy cdhd chdhch hhhc dhdqw'

stroka = input('input : ')

if stroka.count('f') == 1:
    print('Символ один, выодим = -1')
if stroka.count('f') >= 2:
    print('Символов >= 2, индекс = ', stroka.find('f') + stroka[stroka.find('f')+1:].find('f') +1)
if stroka.count('f') == 0:
    print('Символа f нет, выодим = -2')
