import os
import sys
import shutil
from function_module_3 import account_management
from victory import victorina

personal_account = 0
history_list = []

# 1. Создание папки
def create_a_folder():
    name = input('Введите имя папки  ')
    # проверка на существование
    if not os.path.exists(f'{name}'):
        # создать папку передаем путь
        os.mkdir(f'{name}')
        print(f"Папка {name} создана")
    else:
        print("Такая папка уже есть")


def delete_folder():
    name = input('Введите имя файла/папки  ')
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

def copy_folder():
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
    import os
    import sys

    print('My OS is', sys.platform, '(', os.name, ')')

# os.name, os.uname не работает, а sys.platform врет. показывает 32 разрядную винду, а она 64 разрядная.


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
    print('12. выход')

    choice = input('Выберите пункт меню  ')
    if choice == '1':
        create_a_folder()
    elif choice == '2':
        delete_folder()
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
        personal_account, history_list = account_management(personal_account, history_list)
        print(f'На вашем счету {personal_account} $')
    elif choice == '11':
        change_dir()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')

