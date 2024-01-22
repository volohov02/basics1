import function
import math


# file_name, index, text_string, formula, answer = function.checking_the_answer()
#
# print('Исходный файл:', file_name, ' Вариант №', index)
# print(text_string)
# print('Ответ : ',formula,' = ', answer)
# function.print_rezult_file(file_name, index, text_string, formula, answer)

while True:
    print('1. Создать случайную задачу и вывести в консоль')
    print('2. Создать n случайных задач и записать их с ответами в файл rezult.txt')
    print('3. Создать n случайных задач и записать их в файл task.txt а ответы в файл answer.txt')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только файлы')
    print('6. смена рабочей директории')
    print('7. выход')

    choice = input('Выберите пункт меню  ')
    if choice == '1':
        function.output_console()
    elif choice == '2':
        function.output_one_file()
    elif choice == '3':
        function.output_two_file()
    elif choice == '4':
        function.view_dir()
    elif choice == '5':
        function.view_dir_file()
    elif choice == '6':
        function.change_dir()
    elif choice == '7':
        break
    else:
        print('Неверный пункт меню')