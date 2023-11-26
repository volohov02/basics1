import requests
import pprint
import json

# Здесь собран адрес hh
DOMAIN = 'https://api.hh.ru/'



list_of_vacancies = []
vacancy = 'Python'
area = 1

# Здесь задаются параметры.
params = {'text': vacancy,
          'page': 1,
          'per_page': 100,  # По 100 на странице
          'only_with_salary': True, # Только с указанием зарплаты
          'area': 1 # Только в Москве (а не в Москве никому пайтон разработчики и не нужны...
          }

class HH_servise:

    _url_page = f'{DOMAIN}vacancies'
    def get_page(self, params):
        """
        Здесь получили страницу hh
        param url_vacancies: ссылка на API
        :param params: параметры обращения к API
        :return: страница hh в формате json
        """
        result = requests.get(self._url_page, params = params).json()
        items = result['items']
        return items

    def get_vacancies_by(self, url):
        """
        Передали страницу и номер вакансии, вернули ссылку на эту вакансию
        :param items: страница hh в формате json
        :param item_number: номер вакансии на странице
        :return: ссуылка на конкреную вакансию
        """
        return  requests.get(url).json()

class HH_mapper:
    def map_skills_from(self, vacancies_result):
        """
        Здесь мы из конкретной вакансии вытаскиваем список скиллов
        :param vacancies_result: Ссылка на конкретную вакансию
        :return: список скиллов
        """
        skills = []
        for skill in vacancies_result['key_skills']:
            skills.append(skill['name'])
        return skills

    def get_url_from_page_items_by_index(self, page_items, index):
        return page_items[index]['url']

class Writer:
    def print_skills(self, skills):
        print(skills)
class Main:

    def exec(self, index):
        service = HH_servise()
        hh_mapper = HH_mapper()
        page_items = service.get_page(params)
        vacancies = service.get_vacancies_by(hh_mapper.get_url_from_page_items_by_index(page_items, index))
        skills = hh_mapper.map_skills_from(vacancies)
        #Writer().print_skills(skills)
        return skills

if __name__ == '__main__':
    Main().exec(13)



