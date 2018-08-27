# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)
        self.armor = int(armor)

    def _attack_value(self, who_att, who_def):  # Функция возвращает урон с учетом брони противника
        who_att_k = who_att.damage / who_def.armor
        return who_att_k

    def attack(self, who_att, who_def):  # Функция наносит этот самый урон
        who_def.health -= self._attack_value(who_att, who_def)



class Player(Person):
    pass


class Enemy(Person):
    pass


class War():
    def __init__(self, pl1, pl2):
        self.pl1 = pl1
        self.pl2 = pl2
        self.hit(pl1, pl2)

    def hit(self, pl1, pl2):
        while pl1.health > 0 and pl2.health > 0:
            pl1.attack(pl1, pl2)
            print('Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(pl1.name, pl2.name, pl2.health))

            if pl2.health > 0:
                pl2.attack(pl2, pl1)
                print('Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(pl2.name, pl1.name, pl1.health))

        print('*' * 36)

        if pl1.health > 0:
            print('Игрок {} выиграл! Осталось {} здоровья.'.format(pl1.name, pl1.health))
        else:
            print('Игрок {} выиграл! Осталось {} здоровья.'.format(pl2.name, pl2.health))


pl1 = Player('Алекс', 1000, 50, 2)
en1 = Enemy('Враг', 500, 60, 2.5)
war1 = War(pl1, en1)
