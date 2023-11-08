import requests
import pprint
import json

# Здесь собран адрес hh
DOMAIN = 'https://api.hh.ru/'
url_vacancies = f'{DOMAIN}vacancies'


list_of_vacancies = []
vacancy = 'Python'
area = 1

# Здесь задаются параметры. Правильно под спойлером
params = {'text': vacancy,
          'page': 1,
          'per_page': 100,  # По 100 на странице
          'only_with_salary': True, # Только с указанием зарплаты
          'area': 1 # Только в Москве (а не в Москве никому пайтон разработчики и не нужны...
          }
# class HHService
def get_page(url_vacancies, params):
    """
    Здесь получили страницу hh
    param url_vacancies: ссылка на API
    :param params: параметры обращения к API
    :return: страница hh в формате json
    """
    result = requests.get(url_vacancies, params = params).json() # service
    items = result['items'] # repository
    return items

def get_url(items, item_number):
    """
    Передали страницу и номер вакансии, вернули ссылку на эту вакансию
    :param items: страница hh в формате json
    :param item_number: номер вакансии на странице
    :return: ссуылка на конкреную вакансию
    """
    url = items[item_number]['url'] # repository
    vacancies_result = requests.get(url).json() # repository
    return vacancies_result


#repository
def get_skills(vacancies_result):
    """
    Здесь мы из конкретной вакансии вытаскиваем список скиллов
    :param vacancies_result: Ссылка на конкретную вакансию
    :return: список скиллов
    """
    skills = []
    for skill in vacancies_result['key_skills']:
        skills.append(skill['name'])
    print(skills)
    return skills

# end class

# class HHRepository(HHService)



# repository = HHRepository(HHService())
# repository.get_skills()



# key_error = 0
# index = 0
# while key_error == 0:
#
#     params = {
#         'text': vacancy,
#         # страница
#         'page': index,
#         'per_page': 100, # По 100 на странице
#         'only_with_salary': True, # Только с указанием зарплаты
#         'area': 1 # Только в Москве (а не в Москве никому пайтон разработчики и не нужны...)
#     }
#
#     index += 1

items = get_page(url_vacancies, params)
vacancies_result = get_url(items, 15)
skills = get_skills(vacancies_result)
list_vacancy = []
list_vacancy.append(vacancy)
list_vacancy.append(area)
list_vacancy.append(skills)
print(list_vacancy)
#Тут получился список одной вакансии - вакансия, регион, спискок скиллов
list_of_vacancies.append(list_vacancy)

list_vacancy = []
# А тут уже общий спискок всех вакансий
vacancies_result = get_url(items, 25)
skills = get_skills(vacancies_result)
list_vacancy.append(vacancy)
list_vacancy.append(area)
list_vacancy.append(skills)
print(list_vacancy)
list_of_vacancies.append(list_vacancy)
print(list_of_vacancies)
