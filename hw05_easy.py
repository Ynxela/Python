# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import shutil

for i in range(1, 10):
    os.mkdir('dir_{}'.format(i))

for i in range(1, 10):
    os.rmdir('dir_{}'.format(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for i in os.listdir('.'):
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

file_name = __file__.split('/')[-1:][0]

newfile = file_name + '.copy'
shutil.copy(file_name, newfile)
print('Файл {} был успешно создан.'.format(newfile))