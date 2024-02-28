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

def create_task():
    list_of_file = get_list_of_files()
    file_name, index = select_random_list(list_of_file)
    string_variables, list_of_calc = dictionary_of_variables(file_name)

    list_all = list_of_options(file_name)
    # print(list_all)
    list_options, index = select_random_list(list_all)
    # print(list_options)

    text_string = task_text_generation(list_options, string_variables)
    return file_name, index, text_string

if __name__ == '__main__':
    file_name, index, text_string = create_task()
    print('Исходный файл:', file_name, ' Вариант №', index)
    print(text_string)

