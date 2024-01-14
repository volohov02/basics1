import function
import math

list_of_file = function.get_list_of_files()
file_name, index = function.select_random_list(list_of_file)
string_variables, list_of_calc = function.dictionary_of_variables(file_name)

list_all = function.list_of_options(file_name)
# print(list_all)

# обработка рандома из несуществующего списка. Сделать после
list_options, index = function.select_random_list(list_all)
# print(list_options)

text_string = function.task_text_generation(list_options, string_variables)
formula = function.print_file(list_of_calc, index, file_name)
import calculator
answer = math.ceil(calculator.calc() * 100) / 100
if answer > 0:
    print('Исходный файл:', file_name, ' Вариант №', index)
    print(text_string)
    print('Ответ : ',formula,' = ', answer)
    function.print_rezult_file(file_name, index, text_string, formula, answer)
else:
    print('Наша математическая модель не учитывет что результат не должен быть отрицательным, поэтому попробуйте еще раз')
