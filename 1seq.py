list_count = int(input('Введите длину списка - '))

list = []
for index in range (list_count):
    list.append(input(f'Введите {index} элемент списка - '))

print(list)