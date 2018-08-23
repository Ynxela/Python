import os
import shutil


def choose_dir():
    path = input('Введите адрес директории, в которой хотите работать: ')
    if os.path.isdir(path):
        os.chdir(path)
        print('Вы перешли в директорию \'{}\'.'.format(path))
    else:
        print('Такой директории не существует')


def look_dir():
    print(os.listdir('.'))


def create_dir():
    name_dir = input('Введите название для новой папки: ')
    try:
        os.mkdir(name_dir)
        print('Папка \'{}\' успешно создана.'.format(name_dir))
    except OSError:
        print('Папка \'{}\' уже существует.'.format(name_dir))


def del_dir():
    name_dir = input('Введите название папки, которую хотите удалить: ')
    if name_dir in os.listdir('.'):
        if os.path.isdir(name_dir):
            shutil.rmtree(name_dir)
            print('Папка \'{}\' успешно удалена.'.format(name_dir))
        else:
            print('\'{}\' не является папкой. Удалить нельзя!'.format(name_dir))
    else:
        print('Папки \'{}\' не существует.'.format(name_dir))
