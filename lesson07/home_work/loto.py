#!/usr/bin/python3
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных
цифр,
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
from random import randint

class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]  # Мешок с бочками.
        self.card = [__class__.gen_string(bag), __class__.gen_string(bag),
                     __class__.gen_string(bag)]
        self.name = name
        self.count_barrel = 15  # осталось бочек на карточке

    @staticmethod
    def gen_string(bag):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digit = randint(0, x)
            while string[digit] != '':
                digit += 1
            string[digit] = bag.pop(randint(0, len(bag) - 1))
        return string

    def __str__(self):
        rez = f'{self.name:=^27}\n'
        for x in range(3):
            rez += '{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'\
                    .format(*self.card[x]) + '\n'
        return rez + '---------------------------'

    def barell_in_card(self, barrel):
        testy = False
        for x in range(3):
            if barrel in self.card[x]:
                self.card[x][self.card[x].index(barrel)] = 'XX'
                self.count_barrel -= 1
                testy = True
        return testy


computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [x for x in range(1, 91)]  # Мешок с бочками.
time_game = True
while time_game:
    if len(bag) < 1:
        print(f'Бочонки в мешке закончились. Результат:\n'
              f'у компьютера осталось {computer.count_barrel} числа/чисел,\n'
              f'у игрока осталось {player.count_barrel} числа/чисел.'
              )
        time_game = False
    barrel = bag.pop(randint(0, len(bag) - 1))
    while True:
        print(f'\nНовый бочонок: {barrel} (осталось {len(bag)})')
        print(computer)
        print(player)
        barrel_for_p = player.barell_in_card(barrel)
        barrel_for_c = computer.barell_in_card(barrel)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()
        if reply == 'q':
            print('Вы вышли из игры. Вы так и не выиграли.')
            time_game = False
            break
        elif reply == 'y':
            if barrel_for_p:
                if player.count_barrel < 1:
                    print('Вы Выиграли!')
                    time_game = False
            else:
                print('Вы програли! Нет такого числа на Вашей карточке!')
                time_game = False
            if computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                time_game = False
            break
        elif reply == 'n':
            if barrel_for_p:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                time_game = False
            if computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                time_game = False
            break
        if len(reply) == 0 or reply not in 'ynq':
            print('\n\n!!! Ответ не распознан!\n')
