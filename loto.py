#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
  Если цифра есть на карточке - она зачеркивается и игра продолжается.
  Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
  Если цифра есть на карточке - игрок проигрывает и игра завершается.
  Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Card:
    def __init__(self, name, computer=0):
        self.name = name
        self.computer = computer
        self.creating_card()

    def creating_card(self):
        self.main_card = [[' ' for i in range(0, 9)],  # Массив из пустых строк
                          [' ' for i in range(0, 9)],
                          [' ' for i in range(0, 9)]]
        total_numbers = 15  # Количество чисел в массиве main_card
        card_15 = list(random.sample(range(1, 91), total_numbers))  # 15 уникальных элементов
        supercard_15 = sorted(card_15[0:5]) + sorted(card_15[5:10]) + sorted(card_15[10:16])  # Они же, отсортированные

        k = 0
        for line in range(3):
            index_5 = sorted(list(random.sample(range(0, 9), 5)))  # Определяет случайные 5 индексов на строке
            for i in range(5):
                self.main_card[line][index_5[i]] = supercard_15[k]
                k += 1

        return self.main_card

    def show_card(self):

        if self.computer == 0:
            self.nm = 'Человек'
        else:
            self.nm = 'Компьютер'

        st2 = 17 - len(self.name) // 2
        st1 = st2
        if len(self.name) % 2 != 0:
            st1 = st2 - 1

        st4 = 17 - len(self.nm) // 2
        st3 = st4
        if len(self.nm) % 2 != 0:
            st3 = st4 - 1

        print('-' * st1 + ' ' + self.name + ' ' + '-' * st2)

        for i in range(len(self.main_card)):
            for j in range(len(self.main_card[i])):
                print('{:3}'.format(self.main_card[i][j]), end=' ')
            print()

        print('-' * st3 + ' ' + self.nm + ' ' + '-' * st4 + '\n')


class Barrel:
    def __init__(self):
        self.bar()

    def bar(self):
        self.barrel_list = [i for i in range(1, 91)]
        return self.barrel_list

    def step_minus(self):
        self.number = random.choice(self.barrel_list)
        self.barrel_list.remove(self.number)
        return self.number


class MainGame:
    def __init__(self, player=str, opponent=str):
        self.player = player
        self.opponent = opponent
        self.run(player, opponent)

    def check_win(self, z):  # проверяет на вхождение числа в массив, если его нет, то определяет победителя
        x = 0
        for i in range(len(z.main_card)):
            for j in range(len(z.main_card[i])):
                if type(z.main_card[i][j]) is int:
                    x += int((z.main_card[i][j]))
        if x == 0:
            print('Игрок {} выиграл!'.format(z.name))
            return False

    def check(self, x, y):  # проверяет, является игрок человеком или компьютером, дает возможность выбора, если человек
        if x.computer == 0:
            result = 'X'
            while result != 'Y' and result != 'N':
                result = input('Зачеркнуть цифру? (Y/N)')
                if result != 'Y' and result != 'N':
                    print('Не верное значение. Введите Y или N!')

            flag = 0
            if result == 'Y':
                for line in range(len(x.main_card)):
                    if y.number in x.main_card[line]:
                        id = int(x.main_card[line].index(y.number))
                        x.main_card[line][id] = '_'
                        flag = 1
                if flag != 1:
                    print('Игрок {} проиграл!'.format(x.name))
                    return False

            elif result == 'N':
                for line in range(len(x.main_card)):
                    if y.number in x.main_card[line]:
                        print('Игрок {} проиграл!'.format(x.name))
                        return False

        else:
            for line in range(len(x.main_card)):
                if y.number in x.main_card[line]:
                    id = int(x.main_card[line].index(y.number))
                    x.main_card[line][id] = '_'

    def run(self, player, opponent):

        bochka = Barrel()  # Создал список из элементов от 1 до 90

        print('''\nДобро пожаловать в игру!\nДавай дадим игрокам имя и назначим, кто ими управляет!\n''')

        print('Создаем первого игрока: ')
        self.pl_name = input('Введите имя первого игрока: ')
        self.pl_is_comp = int(input('{} - человек или компьютер? 0 - человек, 1 - компьютер: '.format(self.pl_name)))

        print('Создаем второго игрока: ')
        self.op_name = input('Введите имя второго игрока: ')
        self.op_is_comp = int(input('{} - человек или компьютер? 0 - человек, 1 - компьютер: '.format(self.op_name)))

        player = Card(self.pl_name, computer=self.pl_is_comp)
        opponent = Card(self.op_name, computer=self.op_is_comp)

        print('\nНачинаем игру! \n\n')

        while True:

            bochka.step_minus()  # На каждом ходу достает бочку
            print('\n\n\nНовый бочонок: {} (осталось {}) \n'.format(bochka.number, len(bochka.barrel_list)))

            player.show_card()
            opponent.show_card()

            if self.check(player, bochka) is False or self.check(opponent, bochka) is False or self.check_win(
                    player) is False or self.check_win(opponent) is False:
                return False

            print('')


game = MainGame()
