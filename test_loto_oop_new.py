import unittest
#import pytest
from loto_oop_new import Barrel, list_random, BarrelRandom, Card, Game, GameIO
from random import randint

def test_list_random():
    list_numbers = list_random(5,1,90)
    # print(list_numbers)
    assert len(list_numbers) == 5
    for index in range(5):
        assert list_numbers[index] >=1 and list_numbers[index] <=90

class TestBarrelRandom:

    def __str__(self):
        barrel_random = BarrelRandom()
        barrel_random = str(barrel_random)
        hash_barrel_random = hash(barrel_random)
        self.assertEqual(barrel_random, f'Это магический метод класса BarrelRandom. Хэш: {hash_barrel_random}')

    counter = 0
    def get_rand_number(self):
        self.counter = self.counter + 1
        return self.counter

    def test_get_rand_number(self):
        barrelrandom = BarrelRandom()
        random_number = barrelrandom.get_rand_number()
        assert random_number >= 1 and random_number <= 90

class TestBarrel(unittest.TestCase):

    def test_init(self):

        self.barrel = Barrel(0, [], TestBarrelRandom())
        self.barrel.generation_of_move()
        move_number = self.barrel.generation_of_move()
        self.assertEqual(move_number,2)

    def __str__(self):
        barrel = Barrel()
        barrel = str(barrel)
        self.assertEqual(barrel, 'Это магический метод класса Barrel. Выпал номер 0')
        move_number = barrel.generation_of_move()
        self.assertEqual(barrel, 'Это магический метод класса Barrel. Выпал номер {move_number}')

class TestCard(unittest.TestCase):

    def setUp(self):
        self.test_card = Card()

    def __str__(self):
        test_card = str(test_card)
        self.assertEqual(test_card, 'Это магический метод класса Card.')

    def test_init(self):
        #print(self.test_card.values)
        for index_string in range(3):
            for index_columns in range(9):
                self.assertEqual(self.test_card.values[index_string][index_columns][0], None)
                self.assertEqual(self.test_card.values[index_string][index_columns][1], True)

    def test_generation_of_card(self):
        self.test_card.generation_of_card()
        count_1 = 0
        for index_string in range(3):
            for index_columns in range(9):
                if self.test_card.values[index_string][index_columns][0] != None:
                    count_1 += 1
        self.assertEqual(count_1, 15)

    def test_chekin_card(self):
        self.test_card.generation_of_card()
        count_1 = 0
        for index_string in range(3):
            for index_columns in range(9):
                if self.test_card.values[index_string][index_columns][1] != 'True':
                    count_1 += 1
        self.assertEqual(count_1, 27)


    def test__eq__(self):
        computer_card = Card()
        computer_card.generation_of_card()
        human_card = computer_card
        self.assertTrue (computer_card.__eq__(human_card))
        human_card = Card()
        human_card.generation_of_card()
        self.assertFalse(computer_card.__eq__(human_card))





class TestGame(unittest.TestCase):

    def __str__(self):
        game = Game()
        game = str(game)
        self.assertEqual(game, 'Это магический метод класса Game.')
    pass

    def test_computer_moving(self):
        self.game_io = GameIO()
        self.computer_card = Card()
        self.human_card = Card()
        self.game = Game(self.computer_card, self.human_card, self.game_io)

        self.computer_card.generation_of_card()
        list_string = []
        for index_columns in range(9):
            if self.computer_card.values[0][index_columns][0] != None:
                list_string.append(self.computer_card.values[0][index_columns][0])
        #print(list_string)
        num = randint(0,4)
        self.game.computer_moving(list_string[num])
        #self.computer_card.print_of_card()
        count_1 = 0
        for index_string in range(3):
            for index_columns in range(9):
                if self.computer_card.values[index_string][index_columns][1] != True:
                    count_1 += 1
        self.assertEqual(count_1, 1)


    def test_computer_moving(self):
        self.game_io = GameIO()
        self.computer_card = Card()
        self.human_card = Card()
        self.game = Game(self.computer_card, self.human_card, self.game_io)

class TestGameIO(unittest.TestCase):

    def __str__(self):
        gameio = GameIO()
        gameio = str(gameio)
        self.assertEqual(gameio, 'Это магический метод класса GameIO.')