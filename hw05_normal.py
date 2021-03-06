# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import easy

while True:
    action = int(input('''
    Выберите действие:
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Создать папку
    4. Удалить папку
    5. Завершить программу
    '''))

    print('')
    if action == 1:
        easy.choose_dir()
    elif action == 2:
        easy.look_dir()
    elif action == 3:
        easy.create_dir()
    elif action == 4:
        easy.del_dir()
    elif action == 5:
        break


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
