import random
def victorina():

        list = ['Пушкин Александр Сергеевич;06.06.1977; шестого июня 1977 года',
                'Королёв Сергей Павлович; 30.12.1906;тридцатого декабря 1906 года',
                'Гагарин Юрий Алексеевич;09.03.1934;девятого марта 1934 года',
                'Ленин Владимир Ильич;10.04.1870;десятого апреля 1870 года',
                'Сталин Иосиф Виссарионович;09.12.1879;девятого декабря 1879 года',
                'Карл Генрих Маркс;14.03.1833;четырнадцатого марта 1883 года',
                'Фридрих Энгельс;05.08.1895;пятого августа 1895 года',
                'Никита Сергеевич Хрущёв;03.04.1984;третьего апреля 1894 года',
                'Мао Цзэдун;26.12.1893;двадцать шестого декабря 1893 года',
                'Джон Уинстон Леннон;09.10.1940;девятого октября 1940 года']

        play = 'yes'
        while play == 'yes':

                numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                result = random.sample(numbers, 5)

                #print(result)

                true_answer = 0
                for index in range (0,5):
                    person_list = list[result[index]].split(';')

                    year = input(f'Когда родился {person_list[0]} в формате dd.mm.yyyy - ')
                    if (year != person_list[1]):
                            print('Фиг ты угадал!')
                            print(f'{person_list[0]} родился {person_list[2]}')
                    else:
                            true_answer +=1

                print(f'Правильных ответов {true_answer} из 5')
                print(f'Неравильных ответов {5-true_answer} из 5')
                print('Процент правильных ответов: ', true_answer * 20)
                print('Процент неправильных ответов: ', 100 - true_answer * 20)
                play = input('Хотите сыграть еще? yes/no - ')
