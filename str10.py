#!/usr/bin/env python

# задание 10

"""
Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое
и последнее вхождение буквы h, а также все символы, находящиеся между ними.
"""

# stroka = 'skfjh dcsh cdhd chfdhch hhhcf dhfdqw'

stroka = input('input : ')

print('Удалили символы h и между ними = ', stroka[:stroka.find("h")]+stroka[stroka.rfind("h")+1:])
