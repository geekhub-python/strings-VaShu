#!/usr/bin/env python

# задание 11

"""
Дана строка, в которой буква `h` встречается как минимум два раза. Разверните последовательность
символов, заключенную между первым и последнием появлением буквы `h`, в противоположном порядке.
"""

# stroka = 'skfjh1dcsh cdhd chfdhch hhhcf9hfdqw'

stroka = input('input : ')
reversi = stroka[stroka.find("h")+1:stroka.rfind("h")]
print('Реверс символов между первым и последним h = ', reversi[::-1])
