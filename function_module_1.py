#1
def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    separator = '*' * 10
    return separator

print(simple_separator())

print(simple_separator() == '**********')  # True

#2
def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """

    separator = '*' * count
    return separator

print(long_separator(7))
print(long_separator(2))
print(long_separator(12))

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

#3
def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    separat = simbol * count
    return separat

print(separator('&',12))

print(separator('-', 10) == '-----6----')  # True
print(separator('#', 5) == '#####')  # True

#4 Просто интересно функцию в функции. На самом деле проще было бы стрингом в лом звездочки вывести.
def hello_world(separator, count=10):
    """
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """
    print(separator('*', 10), '\n')
    print('Hello World! \n')
    print(separator('#', 10))


'''
**********
Hello World!
##########
'''
hello_world(separator,10)


#5
def hello_who(separator, count=10, who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print(separator('*', 10), '\n')
    print('Hello', who, '\n')
    print(separator('#', 10))

hello_who(separator, 10, 'Max')

#6
def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    result = 0
    for number in args:
        result += number
    result = result**power
    return result


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

print(pow_many(2, 1, 2, 3, 4) )

#7
def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for k, v in kwargs.items():
        print(f'{k} --> {v}')


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)

#8
def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    new_list = list(filter(function, iterable))
    return new_list


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True