# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def attack(attack_arg, defend_arg):
    defend_arg['health'] -= attack_arg['damage']
    print(defend_arg)


name_p = input('Дай имя игроку: ')
name_e = input('Дай имя врагу: ')

player = {'name': name_p, 'health': 100, 'damage': 50}
enemy = {'name': name_e, 'health': 100, 'damage': 50}

attack(player, enemy)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


def attack_value(attack_arg, defend_arg):  # Вычисляет урон по отношению к броне
    attack_arg['attack'] /= defend_arg['defend']
    return attack_arg['attack']


def attack(attack_arg, defend_arg):  # Наносит урон!
    defend_arg['health'] -= attack_value(attack_arg, defend_arg)


keys_players = ['name', 'health', 'attack', 'defend']

name_pl = input('Введите имя игрока: ')
health_pl = int(input('Введите жизни игрока: '))
attack_pl = int(input('Введите атаку игрока: '))
def_pl = float(input('Введите броню игрока: '))
player_stats = [name_pl, health_pl, attack_pl, def_pl]
player = dict(zip(keys_players, player_stats))
file = open('player.txt', 'w')
for key, val in player.items():
    file.write('{} - {}\n'.format(key, val))
file.close()

name_enem = input('Введите имя врага: ')
health_enem = int(input('Введите жизни врага: '))
attack_enem = int(input('Введите атаку врага: '))
def_enem = float(input('Введите броню врага: '))
enemy_stats = [name_enem, health_enem, attack_enem, def_enem]
enemy = dict(zip(keys_players, enemy_stats))
file = open('enemy.txt', 'w')
for key, val in enemy.items():
    file.write('{} - {}\n'.format(key, val))
file.close()

file = open('player.txt')
for i in file.readlines():
    key, val = i.strip().split(' - ')
    player[key] = val
    player['health'] = int(player['health'])
    player['attack'] = int(player['attack'])
    player['defend'] = float(player['defend'])
file.close()

file = open('enemy.txt')
for i in file.readlines():
    key, val = i.strip().split(' - ')
    enemy[key] = val
    enemy['health'] = int(enemy['health'])
    enemy['attack'] = int(enemy['attack'])
    enemy['defend'] = float(enemy['defend'])
file.close()

while player['health'] > 0 and enemy['health'] > 0:
    attack(player, enemy)
    print(
        'Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(player['name'], enemy['name'], enemy['health']))
    if enemy['health'] > 0:
        attack(enemy, player)
        print('Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(enemy['name'], player['name'],
                                                                              player['health']))

if player['health'] > 0:
    print('Игрок {} выиграл! Осталось {} здоровья.'.format(player['name'], player['health']))
else:
    print('Игрок {} выиграл! Осталось {} здоровья.'.format(enemy['name'], enemy['health']))
