# Задача №1
# filename: hw_1_1.py

# Запросить у пользователя имя и фамилию.
# Поприветсвовать пользователя с использованием его имени и фамилии.
# Запросить День даты рождения (цело число).
# Запросить Месяц даты рождения (цело число).
# Запросить Год даты рождения (цело число).
# Вывести количество прожитых лет (цело число).
# Вывести количество прожитых месяцев (цело число).
# Вывести количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019 - без учёта високосных лет и считая, что среднее количество дней в месяце = 30.

name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
print( 'Привет,', name, surname)

day1 = input('День даты рождения: ')
month1 = input('Месяц даты рождения: ')
year1 = input('Год даты рождения: ')

day2 = 31
month2 = 1
year2 = 2019

import math

years_total = int(year2)-int(year1) - math.fabs(int(month2)-int(month1))/12
print('Количество прожитых лет:', int(years_total))
months_total = 12 * int(years_total) + math.fabs(int(month2)-int(month1))
print('Количество прожитых месяцев:', int(months_total))
days_total = 30 * int(months_total) + math.fabs(int(day2)-int(day1))
print('Количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019: ', int(days_total),',', int(months_total),',', int(years_total))