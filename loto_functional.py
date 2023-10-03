from random import randint

columns = 9
lines = 3
max_count = 90
min_count = 1
count_in_line = 5
move_history = []

# Warning!  count_in_line*lines <= max_count - min_count
# Warning!  len(move_history) <= max_count - min_count

# Непубличная функция?
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

def generation_of_array(lines,columns):
    """
    Генерация массива columns*lines из [None,True]
    :param lines: число строк
    :param columns: число колонок
    :return: пустая карточка
    """
    null_card = [[[None,True] for j in range(columns)] for i in range(lines)]
    return null_card

def generation_of_card(card, min_count, max_count, columns, lines, count_in_line):
    """
    Заполнение карточки рандомными значениями по 5 в строке без повторений
    :param card: карточка
    :return: карточка
    """
    list_15_90 = list_random(count_in_line*lines, min_count, max_count)
    #print(list_15_90)
    for index_string in range(lines):
        list_5_9 = list_random(count_in_line, 0, columns-1)
        #print(list_5_9)
        for index_list in range(count_in_line):
            card[index_string][list_5_9[index_list]][0] = list_15_90[index_list+index_string*count_in_line]
    return card

def print_of_card(card, columns, lines):
    """
    Вывод карточки в консоль
    :param card: Карточка
    :return: ---
    """
    print('-'*columns*3)
    for index_string in range(lines):

        card_string = ''
        for index_column in range(columns):
            if card[index_string][index_column][1] == False:
                card_string += ' --'
            else:
                choise = card[index_string][index_column][0]
                if choise == None:
                    card_string += '   '
                elif choise < 10:
                    card_string += '  '+ str(card[index_string][index_column][0])
                elif choise >= 10:
                    card_string += ' ' + str(card[index_string][index_column][0])
        print(card_string)
    print('-'*columns*3)

def generation_of_move(move_history, min_count, max_count):
    """
    Генерирует ход
    :param move_history: история ходов
    :return: число в качестве хода
    """
    number = randint(min_count, max_count)
    while number in move_history:
        number = randint(min_count, max_count)
    move_history.append(number)
    return number

def computer_moving(card, move_number, columns, lines):
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
            if card[index_string][index_columns][0] == move_number:
                card[index_string][index_columns][1] = False
    return card

def human_moving(card, move_number, columns, lines):
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
    human_error = 3
    for index_string in range(lines):
        for index_columns in range(columns):
            if (card[index_string][index_columns][0] == move_number and move == 'y'):
                card[index_string][index_columns][1] = False
                human_error = 0
            elif card[index_string][index_columns][0] == move_number and move != 'y':
                human_error = 1
    if human_error == 3 and move == 'y':
        human_error = 1
    elif human_error != 1:
        human_error = 0

    return card, human_error

def chekin_card(card):
    """
    Проверяет количество зачеркнутых элементов
    :param card: карточка
    :return: количество зачеркнутых элементов
    """
    namber = 0
    for index_string in range(lines):
        for index_columns in range(columns):
            if (card[index_string][index_columns][1] == False):
                namber += 1
    return namber


check_computer = 0
check_human = 0
human_error = 0

computer_card = generation_of_array(lines, columns)
computer_card = generation_of_card(computer_card, min_count, max_count, columns, lines, count_in_line)
human_card = generation_of_array(lines, columns)
human_card = generation_of_card(human_card, min_count, max_count, columns, lines, count_in_line)
print('Карточка компьютера')
print_of_card(computer_card, columns, lines)
print('Карточка человека')
print_of_card(human_card, columns, lines)

while check_computer < count_in_line*lines and check_human < count_in_line*lines and human_error == 0:
    move_number = generation_of_move(move_history, min_count, max_count)
    computer_card = computer_moving(computer_card, move_number, columns, lines)
    human_card, human_error = human_moving(human_card, move_number, columns, lines)
    print('Карточка компьютера')
    print_of_card(computer_card, columns, lines)
    print('Карточка человека')
    print_of_card(human_card, columns, lines)
    check_computer = chekin_card(computer_card)
    check_human = chekin_card(human_card)

print('Game over')
print('Computer Win!') if check_computer == count_in_line*lines or human_error == 1 else print('Human Win!')


