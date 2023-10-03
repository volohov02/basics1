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
class Barrel:
    # Переменные класса "бочонок" не должны меняться снаружи класса.


    def __init__(self, number=0, move_history=[]):
        self.__number = number
        self.__move_history = move_history

    def generation_of_move(self):
        self.__number = randint(min_count, max_count)
        while self.__number in self.__move_history:
            self.__number = randint(min_count, max_count)
        self.__move_history.append(self.__number)
        move_namber = self.__number
        return move_namber

#--------------------------------------------------------------------------------

class Card:

    def __init__(self):
        self.card = [[[None, True] for j in range(columns)] for i in range(lines)]
        self.human_error = 3

    def print_list_card(self):
        print(self.card)

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
                self.card[index_string][list_5_9[index_list]][0] = list_15_90[index_list+index_string*count_in_line]

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
                if self.card[index_string][index_column][1] == False:
                    card_string += ' --'
                else:
                    choise = self.card[index_string][index_column][0]
                    if choise == None:
                        card_string += '   '
                    elif choise < 10:
                        card_string += '  '+ str(self.card[index_string][index_column][0])
                    elif choise >= 10:
                        card_string += ' ' + str(self.card[index_string][index_column][0])
            print(card_string)
        print('-'*columns*3)
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
                if self.card[index_string][index_columns][0] == move_number:
                    self.card[index_string][index_columns][1] = False

    def human_moving(self,move_number):
        """
        Ходит за человека, требует ввод
        :param card: карточка
        :param move_number: выпавший номер
        :param columns: колонки
        :param lines: строки
        :return: Карточка
        """
        print(f'Выпал номер  {move_number}')
        move = input('Зачеркнуть цифру? (y/n) ')
        for index_string in range(lines):
            for index_columns in range(columns):
                if (self.card[index_string][index_columns][0] == move_number and move == 'y'):
                    self.card[index_string][index_columns][1] = False
                    self.human_error = 0
                elif self.card[index_string][index_columns][0] == move_number and move != 'y':
                    self.human_error = 1
        if self.human_error == 3 and move == 'y':
            self.human_error = 1
        elif self.human_error != 1:
            self.human_error = 0
        return self.human_error

    def chekin_card(self):
        """
        Проверяет количество зачеркнутых элементов
        :param card: карточка
        :return: количество зачеркнутых элементов
        """
        namber = 0
        for index_string in range(lines):
            for index_columns in range(columns):
                if (self.card[index_string][index_columns][1] == False):
                    namber += 1
        return namber

check_computer = 0
check_human = 0
human_error = 0

computer_card = Card()
computer_card.generation_of_card()
human_card = Card()
human_card.generation_of_card()
print('Карточка компьютера')
computer_card.print_of_card()
print('Карточка человека')
human_card.print_of_card()

while check_computer < count_in_line*lines and check_human < count_in_line*lines and human_error == 0:
    barrel = Barrel()
    move_number = barrel.generation_of_move()
    computer_card.computer_moving(move_number)
    human_error = human_card.human_moving(move_number)
    print('Карточка компьютера')
    computer_card.print_of_card()
    print('Карточка человека')
    human_card.print_of_card()
    check_computer = computer_card.chekin_card()
    check_human = human_card.chekin_card()

print('Game over')
print('Computer Win!') if check_computer == count_in_line*lines or human_error == 1 else print('Human Win!')