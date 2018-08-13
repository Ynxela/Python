﻿# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


# Создадим список, используя разделитель - пробел.
equat_list = equation.split(' ')

# b - это 4 элемент из списка
b = float(equat_list[4])

# k - Возьмем 3 элемент, его снова разделим, (х - разделитель), возьмем k.
k = int((equat_list[2]).split('x')[0])

y = k * x + b

print('Координата y = {}'.format(y))









# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


date = input('Введите дату строго в формате dd.mm.yyyy: ')

date_list = date.split('.')  # Создал списоок из д, м, г

days = {
    '01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30,
    '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31
}

print(date)
k = False  # k - индикатор истинности, иститен, если все условия выполняются.

if 1 <= int(date_list[1]) <= 12 and len(date_list[1]) == 2:  # 12 месяцев - максимум.
    if 1 <= int(date_list[0]) <= days[date_list[1]] and len(date_list[0]) == 2:  #max в зависимости от месяца
        if 1 <= int(date_list[1]) <= 9999 and len(date_list[2]) == 4:
            k = True

if k == True:
    print('Дата введена корректно!')
else:
    print('Дата введена некорректно, исправь!')









# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3