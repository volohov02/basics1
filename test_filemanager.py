def test_author_info():
    assert author_info() == 'Author Leo'

#Чистых функций нет, все они затрагивают "окружающий мир"...
#Хуже того, в счете функции лежат внутри функций и не очень понятно, как их импортировать...
#author_info  не тянет на функцию, это один оператор print. Заводить на него переменную и функцию ради теста странно.

from function_module_3 import history

def test_history():
    test_history_1 = ['Пушкин','Непушкин']
    test_history_2 = [1,2,3]
    test_data_1 = history(test_history_1)
    test_data_2 = history(test_history_2)
    assert test_data_1 == ['1. Пушкин', '2. Непушкин']
    assert test_data_2 == ['1. 1', '2. 2', '3. 3']

# В итоге в функцию, которую и в функцию бы выделять не стоило пришлось добавить следующие операторы, чтобы она хоть что-то возвращала.
#    test_date = []
#        test_date.append(f'{index+1}. {history_list[index]}')
#    return test_date

#Ну, в учебных целях оно, конечно, да... Но по мне я бы в пункт "история покупок" просто поставил бы
#    for index in range(len(history_list)):
#        print(index+1,". ",history_list[index])
# И не нужна она та функция...

import os
import sys
import shutil

from file_manager import create_a_folder, delete_folder

def test_create_a_folder():
    if os.path.isdir('name') != True:
        create_a_folder('name')
        assert os.path.isdir('name')
    else:
        print('Папка уже есть')

def test_create_a_folder_1():
    if os.path.isdir('name') != True:
        create_a_folder('name')
        assert os.path.isdir('name')
    else:
        print('Папка уже есть')

#Вот тут я красавчег! Если папки нет, то тест пройден, но с надписью папака создана, если она уже есть, то тоже пройден с сообщением, что она уже есть.
# Тест один и тот же, но первый проходит когда папки нет, а второй, когда она создана при первом тесте.


def test_delete_folder():
    if os.path.isdir('name') == True:
        delete_folder('name')
        assert os.path.isdir('name') != True
    else:
        print('Такой папки нет')

def test_delete_folder_1():
    if os.path.isdir('name') == True:
        delete_folder('name')
        assert os.path.isdir('name') != True
    else:
        print('Такой папки нет')

#Аналогично для других системных функций.
#Вообще, в силу того, что программа мелкая, модульное тестирование одновременно является и приемочным. Оно же ручное... Тем более написанный код в каждой ветке if сообщает что произошло - папка удалена, папка не удалена, потому что ее не было, и т.д.
#Домашнее задание выглядит извращением, на самом деле каждую функцию я тестил вручную (веток мало) после написания. Выводы - код плохой, чистых функций нет, автоматически тестировать не удобно. Писать надо изначально ориентируясь на автоматическое тестирование.
# Стал бы я писать именно это задание иначе? Нет, не стал бы. А вот что-нибудь содержащее громоздкие вычислния, преобразования массивов и т.д, где связь входа и выхода не так очевидно надо сразу писать чисто с расчетом на автоматический тест.