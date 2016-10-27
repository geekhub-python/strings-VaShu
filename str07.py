#!/usr/bin/env python

# задание 7

"""
Дана строка. Замение в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""

stroka = 'fskfjh dcsh cdhd chdhch hhhc dhdqw'
x = stroka.find('h')
y = stroka.rfind('h')
new = stroka[:x+1] + stroka[x + 1: y].replace('h', 'H') + stroka[y:]
print('Замена h на H = ', new)
