#!/usr/bin/env python

# задание 4

"""
Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова
местами. Результат запишите в строку и выведите получившуюся строку.

Задача должна быть решена без использования оператора if
"""

stroka = 'Hello, world!'
print('Реверс слов = ',
      stroka[stroka.find(' ') + 1:] + stroka[stroka.find(' '):stroka.find(' ') + 1] + stroka[:stroka.find(' ')])