list_string = input('Введите цифры через запятую - ')
list_string = list_string.replace(';',',').replace('/',',')
list = list_string.split(',')

index = 0

while index <  (len(list)):
    if (list.count(list[index])) > 1:
        list.remove(list[index])
    else:
        index += 1

print(list)