# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки.")
    print("mkdir <dir_name> - создание директории.")
    print("ping - тестовый ключ.")
    print('cp <file_name> - создает копию указанного файла.')
    print('rm <file_name> - удаляет указанный файл.')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную.')
    print('ls - отображение полного пути текущей директории.')


def file_copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром.")
        return
    try:
        newfile = file_name + '.copy'
        shutil.copy(file_name, newfile)
        if os.path.exists(newfile):
            print('Файл \'{}\' был успешно создан.'.format(newfile))
        else:
            print('Возникли проблемы копирования.')
    except FileExistsError:
        print('файла \'{}\' не существует.'.format(file_name))


def file_remove():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        ans = input('Вы действительно хотите удалить {} Y/N?'.format(file_name))
        if ans == 'Y':
            os.remove(file_name)
            print('Файл \'{}\' удален.'.format(file_name))
        else:
            return
    except FileExistsError:
        print('Файл \'{}\' не существует.'.format(file_name))


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория \'{}\' создана'.format(dir_name))
    except FileExistsError:
        print('Директория \'{}\' уже существует'.format(dir_name))


def choose_dir():
    if os.path.isdir(sys.argv[2]):
        os.chdir(sys.argv[2])
        print('Вы перешли в директорию \'{}\'.'.format(sys.argv[2]))
    else:
        print('Такой директории не существует')


def full_path():
    print(os.getcwd())


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': file_copy,
    'rm': file_remove,
    'cd': change_dir,
    'ls': full_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

# P.S. По возможности, сделайте кросс-платформенную реализацию.
