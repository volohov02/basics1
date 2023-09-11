play = 'yes'
true_answer = 0
false_answer = 0
answer = 0

while play == 'yes':
    year = input('Введите год рождения Пушкина - ')
    # 1799
    answer += 1
    if (year == '1799'):
        print('Верно')
        true_answer += 1
    else:
        print('Неверно')
        false_answer += 1

    year = input('Введите год рождения Королева (Виктора Павловича!) - ')
    # 1907
    answer += 1
    if (year == '1907'):
        print('Верно')
        true_answer += 1
    else:
        print('Неверно')
        false_answer += 1

    year = input('Введите год рождения Ленина - ')
    # 1870
    answer += 1
    if (year == '1870'):
        print('Верно')
        true_answer += 1
    else:
        print('Неверно')
        false_answer += 1

    year = input('Введите год рождения Леннона - ')
    # 1940
    answer += 1
    if (year == '1940'):
        print('Верно')
        true_answer += 1
    else:
        print('Неверно')
        false_answer += 1

    year = input('Введите год рождения Гагарина (Юрия Алексеевича) - ')
    # 1954
    answer += 1
    if (year == '1954'):
        print('Верно')
        true_answer += 1
    else:
        print('Неверно')
        false_answer += 1

    print('Всего ответов: ', 5)
    print('Правильных ответов: ', true_answer)
    print('Неправильных ответов: ', false_answer)
    print('Процент правильных ответов: ', true_answer*100/5)
    print('Процент неправильных ответов: ', false_answer*100/5)
    play = input('Хотите сыграть еще? yes/no - ')

