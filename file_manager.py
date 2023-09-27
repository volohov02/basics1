import os
import sys
import shutil
from function_module_3 import account_management
from victory import victorina

personal_account = 0
history_list = []

#0. декоратор
def advertising(func):
    def inner(*args, **kwargs):
        print('*'*45)
        print('Это РЕКЛАМА и уберем мы ее если нам заплатят!')
        print('*'*45)
        result = func(*args, **kwargs)
        return result
    return inner

# 1. Создание папки
@advertising
def create_a_folder(name):
#Тернарный оператор. Пришлось пожертвовать сообщением, что папка создана
# Больше конструкций if - else с одним оператором в каждой ветке нет. Делать искусственно тернарный оператор из if без else не вижу смысла
    os.mkdir(f'{name}') if not os.path.exists(f'{name}') else print("Такая папка уже есть")
    # #name = input('Введите имя папки  ')
    # # проверка на существование
    # if not os.path.exists(f'{name}'):
    #     # создать папку передаем путь
    #     os.mkdir(f'{name}')
    #     print(f"Папка {name} создана")
    # else:
    #     print("Такая папка уже есть")


def delete_folder(name):
    # проверка на существование
    if os.path.exists(f'{name}'):
        # удалить папку
        if os.path.isdir(name):
            shutil.rmtree(f'{name}')
            print(f"папка {name} удалена")

# По-хорошему, тут бы проверить пустая папка или нет
#Функция rmdir() модуля os удаляет путь к каталогу path.
# Если директория path не является пустым каталогом, соответственно возникает исключение OSError.
# А уже его можно обрабатывать shutil.rmtree

        elif os.path.isfile(name):
            os.remove(f'{name}')
            print(f"Файл {name} удален")
        else:
            print('Это не файл и не папка!')

    else:
        print("Такого(ой) файла/папки нет")

@advertising
def copy_folder(name):
    name = input('Введите имя файла/папки  для копирования  ')
    # проверка на существование
    if os.path.exists(f'{name}'):
        if os.path.isdir(name):
            new_name = name + ' copy'
            shutil.copytree(name, new_name)
            print(f"Папка {name} скопирована в папку {new_name}")
        elif os.path.isfile(name):
            base, ext = os.path.splitext(name)
            new_name = base + ' copy' + ext
            shutil.copy(name, new_name)
            print(f"Файл {name} скопирован в файл {new_name}")
        else:
            print('Это не файл и не папка!')
    else:
        print("Такого(ой) файла/папки нет")


def view_dir():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        print(index)

@advertising
def view_dir_folder():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        if os.path.isdir(index):
            print(index)

def view_dir_file():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    for index in sortetd_file_list:
        if os.path.isfile(index):
            print(index)

def info_os():
    print('My OS is', sys.platform, '(', os.name, ')')

# os.name, os.uname не работает, а sys.platform врет. показывает 32 разрядную винду, а она 64 разрядная.


# Здесь уже реализована обработка исключений

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

# В плане усложнения не понял - 'C:\Users\Александр\PycharmProjects\pythonProject1\basics1\venv' меняет каталог с basics1 на venv
#  и просто 'venv' меняет каталог на venv. В принципе не вижу проблемы в парсинге пути и, например, использовании стрелочки для "назад"

def print_dir():
    unsorted_file_list = os.listdir()
    sortetd_file_list = sorted(unsorted_file_list)
    with open('listdir.txt', 'w') as f:
        f.write('files: ')
        for index in sortetd_file_list:
            if os.path.isfile(index):
                f.write(f'{index}, ')
        f.write('\n')
        f.write('dirs:  ')
        for index in sortetd_file_list:
            if os.path.isdir(index):
                f.write(f'{index}, ')


if __name__ == '__main__':
    while True:
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. смена рабочей директории')
        print('12. сохранить содержимое рабочей директории в файл')
        print('13. выход')

        choice = input('Выберите пункт меню  ')
        if choice == '1':
            name = input('Введите имя папки  ')
            create_a_folder(name)
        elif choice == '2':
            name = input('Введите имя файла/папки  ')
            delete_folder(name)
        elif choice == '3':
            copy_folder()
        elif choice == '4':
            view_dir()
        elif choice == '5':
            view_dir_folder()
        elif choice == '6':
            view_dir_file()
        elif choice == '7':
            info_os()
        elif choice == '8':
            print('Я - создатель программы. Волохов А.А')
        elif choice == '9':
            victorina()
        elif choice == '10':
            account_management()
            # print(f'На вашем счету {personal_account} $')
        elif choice == '11':
            change_dir()
        elif choice == '12':
            print_dir()
        elif choice == '13':
            break
        else:
            print('Неверный пункт меню')

