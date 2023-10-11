from random import randint


def list_random(list_lenth, begin, end):
    """
    :param list_lenth: длина рандомного списка
    :param begin: минимальное значение
    :param end: максимальное значение
    :return: случайный список без повторов
    """
    list_numbers = []
    while len(list_numbers) < list_lenth:
        number = randint(begin, end)
        if number in list_numbers:
            pass
        else:
            list_numbers.append(number)
    return list_numbers

min_count = 1
max_count = 90
columns = 9
lines = 3
count_in_line = 5


class BarrelRandom:

    def get_rand_number(self):
        return randint(min_count, max_count)

    def __str__(self):
        return f'Это магический метод класса BarrelRandom. Хэш: {self.__hash__()} '

class Barrel:
    # Переменные класса "бочонок" не должны меняться снаружи класса.


    def __init__(self, number=0, move_history=[], barrel_random = BarrelRandom()):
        self.__number = number
        self.__move_history = move_history
        self.__barrel_random = barrel_random

    def generation_of_move(self):
        self.__number = self.__barrel_random.get_rand_number()
        while self.__number in self.__move_history:
            self.__number = self.__barrel_random.get_rand_number()
        self.__move_history.append(self.__number)
        move_number = self.__number
        return move_number
    def __str__(self):
        return f'Это магический метод класса Barrel. Выпал номер {self.__number}'

#--------------------------------------------------------------------------------



class Card:


    def __eq__(self, other):
        for index_string in range(lines):
            for index_columns in range(columns):
                if (self.values[index_string][index_columns][0] == other.values[index_string][index_columns][0]):
                    return True
                else:
                    return False

    def __str__(self):
        return f'Это магический метод класса Card.'

    def __init__(self):
        self.values = [[[None, True] for j in range(columns)] for i in range(lines)]

    def print_list_card(self):
        print(self.values)

    def generation_of_card(self):
        """
        Заполнение карточки рандомными значениями по 5 в строке без повторений
        :param card: карточка
        :return: карточка
        """
        list_15_90 = list_random(count_in_line*lines, min_count, max_count)
        for index_string in range(lines):
            list_5_9 = list_random(count_in_line, 0, columns-1)
            for index_list in range(count_in_line):
                self.values[index_string][list_5_9[index_list]][0] = list_15_90[index_list+index_string*count_in_line]

    def print_of_card(self):
        """
        Вывод карточки в консоль
        :param card: Карточка
        :return: ---
        """
        print('-'*columns*3)
        for index_string in range(lines):

            card_string = ''
            for index_column in range(columns):
                if self.values[index_string][index_column][1] == False:
                    card_string += ' --'
                else:
                    choise = self.values[index_string][index_column][0]
                    if choise == None:
                        card_string += '   '
                    elif choise < 10:
                        card_string += '  '+ str(self.values[index_string][index_column][0])
                    elif choise >= 10:
                        card_string += ' ' + str(self.values[index_string][index_column][0])
            print(card_string)
        print('-'*columns*3)

    def chekin_card(self):
        """
        Проверяет количество зачеркнутых элементов
        :param card: карточка
        :return: количество зачеркнутых элементов
        """
        namber = 0
        for index_string in range(lines):
            for index_columns in range(columns):
                if (self.values[index_string][index_columns][1] == False):
                    namber += 1
        return namber

class Game:

    def __str__(self):
        return f'Это магический метод класса Game.'

    def __init__(self, computer_card, human_card, game_io):
        self.computer_card = computer_card
        self.human_card = human_card
        self.human_error = 3
        self.game_io = game_io

    def computer_moving(self, move_number):
        """
        Ходит за компьютер, не ошибается
        :param card: карточка
        :param move_number: выпавший номер
        :param columns: колонки
        :param lines: строки
        :return: Карточка
        """
        for index_string in range(lines):
            for index_columns in range(columns):
                if self.computer_card.values[index_string][index_columns][0] == move_number:
                    self.computer_card.values[index_string][index_columns][1] = False

    def human_moving(self, move_number):
        """
        Ходит за человека, требует ввод
        :param card: карточка
        :param move_number: выпавший номер
        :param columns: колонки
        :param lines: строки
        :return: Карточка
        """

        move = game_io.apply_number(move_number)
        self.human_error = 3
        for index_string in range(lines):
            for index_columns in range(columns):
                if (self.human_card.values[index_string][index_columns][0] == move_number and move == 'y'):
                    self.human_card.values[index_string][index_columns][1] = False
                    self.human_error = 0
                elif self.human_card.values[index_string][index_columns][0] == move_number and move != 'y':
                    self.human_error = 1
        if self.human_error == 3 and move == 'y':
            self.human_error = 1
        elif self.human_error != 1:
            self.human_error = 0
        return self.human_error

    def game_loop(self):
        check_computer = 0
        check_human = 0
        human_error = 0

        while check_computer < count_in_line * lines and check_human < count_in_line * lines and human_error == 0:
            barrel = Barrel()
            move_number = barrel.generation_of_move()
            game_io.show_computer_card()
            computer_card.print_of_card()
            game_io.show_human_card()
            human_card.print_of_card()
            self.computer_moving(move_number)
            human_error = self.human_moving(move_number)
            check_computer = computer_card.chekin_card()
            check_human = human_card.chekin_card()

        print('Game over')
        print('Computer Win!') if check_computer == count_in_line * lines or human_error == 1 else print('Human Win!')

class GameIO:

    def __str__(self):
        return f'Это магический метод класса GameIO.'

    NUMBER_GET = 'Выпал номер'
    QUESTION_Y_N = 'Зачеркнуть цифру? (y/n) '
    COMPUTER_CARD = 'Карточка компьютера'
    HUMAN_CARD = 'Карточка человека'

    def apply_number(self, move_number):
        print(f'{self.NUMBER_GET} {move_number}')
        return input(f'{self.QUESTION_Y_N} ')

    def show_computer_card(self):
        print(self.COMPUTER_CARD)

    def show_human_card(self):
        print(self.HUMAN_CARD)

barrel = Barrel()
print(barrel)
move_number = barrel.generation_of_move()
print(barrel)
barrel_random = BarrelRandom()
print(hash(barrel_random))
print(barrel_random)
gameio = GameIO()
print(gameio)
computer_card = Card()
human_card = Card()
print(computer_card.__eq__(human_card))
game = Game(computer_card, human_card, gameio)
print(game)
card = Card()
print(card)

if __name__ == '__main__':
    computer_card = Card()
    computer_card.generation_of_card()
    human_card = Card()
    human_card.generation_of_card()
    game_io = GameIO()
    game = Game(computer_card, human_card, game_io)
    game.game_loop()

