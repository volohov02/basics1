#Насколько вообще нормально делать функцию в функции? Пайтоном такая конструкция не запрещена, она работает. Стоит ли избегать таких конструкций?
#А вопрос был - как через pytest достучаться, к примеру, до функции purchase, которая находится внутри account_management?
# И вообще - могу ли я как-то импортировать purchase из этой конструкции, игнорируя все остальное?

import os

def account_management():
    FILE_NAME = 'orders.txt'
    number = 0
    personal_account = 0

    # Покупка
    def purchase(number, personal_account):
        money = int(input("Сколько хотите заплатить? "))
        if personal_account < money:
            print("Проваливай, нищеброд!")
        else:
            purchase_name = input("Напишите, как называется ваша покупка: ")
            personal_account -= money
            number += 1
            print(f"Вы купили {purchase_name} на сумму {money} $")
            print("На вашем счету осталось ", personal_account)
        return number, personal_account, money, purchase_name

    # Пополнение счета
    def refill(number, personal_account):
        money = int(input("Введите сумму пополнения: "))
        personal_account += money
        number += 1
        print(f"Ваш счет пополнен на {money} $")
        print("На вашем счету ", personal_account)
        return number, personal_account, money

    # История покупок
    def history(history_list):
        test_date = []
        for index in range(len(history_list)):
            print(index+1,". ",history_list[index])
            test_date.append(f'{index+1}. {history_list[index]}')
        return test_date


    # def account_management():
    #     FILE_NAME = 'orders.txt'
    #     number = 0
    #     personal_account = 0

    orders = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for order in f:
                orders.append(order.replace('\n', ''))
            order = order.replace(': ', '.')
            order = order.split('.')
            number = int(order[0])
            personal_account = int(order[2])

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню  ')
        if choice == '1':
            number, personal_account, money = refill(number, personal_account)
            history_string = (f'{number}.  Баланс : {personal_account}. Ваш счет пополнен на {money} $.')
            orders.append(history_string)
        elif choice == '2':
            number, personal_account, money, purchase_name = purchase(number, personal_account)
            history_string = (f'{number}.  Баланс : {personal_account}.                                    Вы купили {purchase_name} за {money} $.')
            orders.append(history_string)
        elif choice == '3':
            number += 1
            history_string = (f'{number}.  Баланс : {personal_account}.   ------------------ Выведена история операций ----------------------')
            orders.append(history_string)
            for order in orders:
                print(order)

        elif choice == '4':
            number += 1
            history_string = (f'{number}.  Баланс : {personal_account}.   ------------------ Завершена работа программы ----------------------')
            orders.append(history_string)
            with open(FILE_NAME, 'w') as f:
                for order in orders:
                    f.write(f'{order}\n')
            break
        else:
            print('Неверный пункт меню')

account_management()