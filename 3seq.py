list_string_1 = input('Введите цифры списка 1 через запятую - ')
list_string_1 = list_string_1.replace(';',',').replace('/',',')
list_1 = list_string_1.split(',')

list_string_2 = input('Введите цифры списка 2 через запятую - ')
list_string_2 = list_string_2.replace(';',',').replace('/',',')
list_2 = list_string_2.split(',')

index = 0

while index <  (len(list_2)):
    list_1.remove(list_2[index])
    index += 1

print(list_1)