#!/usr/bin/env python3

# Задание 1
str = 'Работа со строками'
print('Третий символ этой строки =', str[2])
print('Предпоследний символ этой строки =', str[-2])
print('Первые пять символов этой строки =', str[0:5])
print('Вся строка, кроме последних двух символов =', str[0:-2])
print('Длина данной строки =', len(str))
print('Все символы с четными индексами =', str[::2])
print('Вывести все символы с нечетными индексами =', str[1::2])
print('Все символы в обратном порядке =', str[::-1])
print('Все символы строки через один в обратном порядке, начиная с последнего =', str[::-2])
