import os
from pathlib import Path
from random import randint
import random
import math
import importlib


def get_list_of_files():
    '''
    :return: список файлов с заданным расширением (fiz)
    '''
    # unsorted_file_list = os.listdir()
    # sorted_file_list = sorted(unsorted_file_list)
    sorted_file_list = os.listdir() #Нам не нужно сортировать список, поэтому сразу так
    list_of_file = []
    for filename in sorted_file_list:
        if os.path.isfile(filename) and Path(filename).suffix == '.fiz':
            list_of_file.append(filename)
    return list_of_file

def select_random_list(list_of_file):
    '''
    :param list_of_file: список
    :return: случайный элемент списка
    '''
    index = randint(0, len(list_of_file)-1)
    return list_of_file[index], index

def random_number(min, max):
    '''
    :param min: минимальное входное значение
    :param max: максимальное входное значение
    :return: случайное число в заданном диапазоне округленное до сотых
    '''
    number = random.random()  # значение от 0.0 до 1.0
    number = math.ceil(((max-min) * number + min)*100)/100
    return number

def dictionary_of_variables(file_name):
    '''
    :param file_name: имя файла для парсинга
    :return: словарь с переменными и их значениями в виде стринга
    '''
    string_variables = dict()

    list_of_calc = []
    flag_string = 0
    flag_var = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for string_line in file:
            if string_line == '<string_variables>\n':
                flag_string = 1
            elif string_line == '</string_variables>\n':
                flag_string = -1
            if flag_string == 1 and string_line != '<string_variables>\n':
                string_line = string_line.replace('\n','')
                list_dict = string_line.split(" = ")
                string_variables[list_dict[0]] = list_dict[1]
            if string_line == '<namber_variables>\n':
                flag_var = 1
            elif string_line == '</namber_variables>\n':
                flag_var = -1
            if flag_var == 1 and string_line != '<namber_variables>\n':
                string_line = string_line.replace('\n', '')
                list_dict = string_line.split(" = ")
                number = random_number(float(list_dict[2]), float(list_dict[3]))
                string_temp = list_dict[1] + ' = ' + str(number) + ' ' + list_dict[4]
                string_variables[list_dict[0]] = string_temp
                string_tmp = '    '+list_dict[1] + ' = ' + str(number)+'\n'
                list_of_calc.append(string_tmp)
        if flag_string != -1 or flag_var != -1:
            print('Нет данных')
    return string_variables, list_of_calc

def list_of_options(file_name):
    list_all = []
    flag_options = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for string_line in file:
            if string_line == '<options>\n':
                flag_options = 1
            elif string_line == '</options>\n':
                flag_options = -1
            if flag_options == 1 and string_line != '<options>\n':
                string_line = string_line.replace('\n','')
                list_dict = string_line.split("=")
                list_all.append(list_dict)
        if flag_options != -1:
            print('Ваша программа упала, потому что в вашем файле нет вариантов')
    return list_all

def task_text_generation(list_options, string_variables):
    text_string = '  '
    for item in list_options:
        text_string = text_string+' '+string_variables[item]
        text_string = text_string.replace(' .','.')
        text_string = text_string.replace(' ,', ',')
    return text_string

def answer_formula(file_name, index):

    list_of_formula = []
    flag_formula = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for string_line in file:
            if string_line == '<answer>\n':
                flag_formula = 1
            elif string_line == '</answer>\n':
                flag_formula = -1
            if flag_formula == 1 and string_line != '<answer>\n':
                string_line = string_line.replace('\n', '')
                list_of_formula.append(string_line)
        if flag_formula != -1:
            print('Ваша программа упала, потому что в вашем файле нет ответов')
        return list_of_formula[index]



def print_file(list_of_calc, index, file_name):
    '''
    Основная задача этого модуля - создание файла calculator.py с функцией calc
    :param list_of_calc: Список формул в файле
    :param index: Номер варианта в файле
    :param file_name: Имя файла
    :return: Разрешающая формула
    '''
    with open('calculator.py', 'w') as f:
        f.write('def calc():\n')
        for item in list_of_calc:
            f.write(item)
        string = answer_formula(file_name, index)
        string_file = '    '+string+'\n'
        f.write(string_file)
        f.write('    return answer')
    return string

def print_rezult_file(file_name, index, text_string, formula, answer):
    '''

    :param file_name: Имя файла
    :param index: Номер варианта в файле
    :param text_string: Текст задачи
    :param formula: Разрешающая формула
    :param answer: Числовой ответ задачи
    :return:
    '''
    with open('rezult.txt', 'a', encoding='utf-8') as f:
        string = 'Исходный файл:'+file_name+' Вариант №'+str(index)+'\n'
        f.write(string)
        text_string = text_string + '\n'
        f.write(text_string)
        string = 'Ответ : '+formula+' = '+str(answer)+'\n'
        f.write(string)
        f.write('\n')

def create_task():
    list_of_file = get_list_of_files()
    file_name, index = select_random_list(list_of_file)
    string_variables, list_of_calc = dictionary_of_variables(file_name)

    list_all = list_of_options(file_name)
    # print(list_all)
    list_options, index = select_random_list(list_all)
    # print(list_options)

    text_string = task_text_generation(list_options, string_variables)
    formula = print_file(list_of_calc, index, file_name)
    import calculator
    answer = math.ceil(calculator.calc() * 100) / 100
    importlib.reload(calculator)
    return file_name, index, text_string, formula, answer

def checking_the_answer():
    answer = 0
    while answer <= 0 or answer > 10000:
        file_name, index, text_string, formula, answer = create_task()
    return file_name, index, text_string, formula, answer

def change_dir():
    print(f'Вы находитесь в каталоге {os.getcwd()}')
    path = input('Введите путь для смены каталога: ')
    try:
        os.chdir(path)
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Каталог: {0} не существует".format(path))
    except NotADirectoryError:
        print("{0} не каталог".format(path))
    except PermissionError:
        print("У вас нет прав на изменение {0}".format(path))

def view_dir_file():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        if os.path.isfile(index):
            print(index)

def view_dir():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        print(index)

def output_console():
    file_name, index, text_string, formula, answer = checking_the_answer()
    print()
    print('Исходный файл:', file_name, ' Вариант №', index)
    print(text_string)
    print('Ответ : ', formula, ' = ', answer)
    print()

def output_one_file():
    name = input('Введите количество задач  ')
    for i in range(int(name)):
        file_name, index, text_string, formula, answer = checking_the_answer()
        print_rezult_file(file_name, index, text_string, formula, answer)
        print('Задача ',i,'успешно добавлена в файл')

def output_two_file():
    name = input('Введите количество задач  ')
    for i in range(int(name)):
        file_name, index, text_string, formula, answer = checking_the_answer()
        string = 'Номер по порядку '+str(i)+'  Исходный файл:' + file_name + ' Вариант №' + str(index) + '\n'
        with open('task.txt', 'a', encoding='utf-8') as f1:
            f1.write(string)
            text_string = text_string + '\n'
            f1.write(text_string)
            f1.write('\n')

        with open('answer.txt', 'a', encoding='utf-8') as f2:
            f2.write(string)
            string = 'Ответ : ' + formula + ' = ' + str(answer) + '\n'
            f2.write(string)
            f2.write('\n')

        print_rezult_file(file_name, index, text_string, formula, answer)
        print('Задача ',i,'успешно добавлена в файл')

if __name__ == '__main__':
    file_name, index, text_string, formula, answer = create_task()
    if answer > 0:
        print('Исходный файл:', file_name, ' Вариант №', index)
        print(text_string)
        print('Ответ : ',formula,' = ', answer)
        print_rezult_file(file_name, index, text_string, formula, answer)
    else:
        print('Наша математическая модель не учитывет что результат не должен быть отрицательным, поэтому попробуйте еще раз')