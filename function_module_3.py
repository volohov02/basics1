def account_management(personal_account=0, history_list=[]):

    # Покупка
    def purchase(personal_account, history_list):
        pay = 'y'
        while pay == 'y':
            money = int(input("Сколько хотите заплатить? "))
            if personal_account < money:
                print("Проваливай, нищеброд!")
            else:
                text = input("Напишите, как называется ваша покупка: ")
                personal_account -= money
                print("На вашем счету осталось ", personal_account)
                history_list.append(f"Вы купили {text} на сумму {money} $")
            pay = input('Хотите продолжить покупки? y/n - ')
        return personal_account, history_list

    # Пополнение счета
    def refill(personal_account, history_list):
        pay = 'y'
        while pay == 'y':
            money = int(input("Введите сумму пополнения: "))
            personal_account += money
            print("На вашем счету ", personal_account)
            history_list.append(f"Ваш счет пополнен на {money} $")
            pay = input('Хотите добавить еще денег? y/n - ')
        return personal_account, history_list

    # История покупок
    def history(history_list):
        for index in range(len(history_list)):
            print(index+1,". ",history_list[index])


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню  ')
        if choice == '1':
            personal_account, history_list = refill(personal_account, history_list)
        elif choice == '2':
            personal_account, history_list = purchase(personal_account, history_list)
        elif choice == '3':
            history(history_list)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    return(personal_account, history_list)



