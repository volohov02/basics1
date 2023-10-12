import requests
import pprint
import json

count_SQL = 0
count_pandas = 0
count_numphy = 0
count_PowerBI = 0
count_python = 0
count_swagger = 0
count_django = 0
count_fastapi = 0
count_tornado = 0
count_React = 0
count_flask = 0
count_sqlalchemy = 0
count_all = 0

result_dict = {'sql': 0,
    'pandas': 0,
    'numphy': 0,
    'powerbi': 0,
    'python': 0,
    'swagger': 0,
    'django': 0,
    'fastapi': 0,
    'tornado': 0,
    'react': 0,
    'flask': 0,
    'sqlalchemy': 0,
    'all': 0
}

def examination(name, snippet):
    if snippet.find(name) != -1:
        result_dict[name] += 1

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'


key_error = 0
index = 0
while key_error == 0:

    params = {
        'text': 'Python',
        # страница
        'page': index,
        'per_page': 100, # По 100 на странице
        'only_with_salary': True, # Только с указанием зарплаты
        'area': 1 # Только в Москве (а не в Москве никому пайтон разработчики и не нужны...)
    }

    index += 1
    try:
        result = requests.get(url_vacancies, params=params).json()
        items = result['items']
        for ind in range (100):
            count_all += 1
            result_dict['all'] += 1
            first = items[ind]
            snippet = str(first['snippet'])
            snippet = snippet.lower()
            examination('sql', snippet)
            examination('pandas', snippet)
            examination('numphy', snippet)
            examination('powerbi', snippet)
            examination('python', snippet)
            examination('swagger', snippet)
            examination('django', snippet)
            examination('fastapi', snippet)
            examination('tornado', snippet)
            examination('react', snippet)
            examination('flask', snippet)
            examination('sqlalchemy', snippet)

    except KeyError:
        key_error = 1
    except IndexError:
        key_error = 1

#print(result_dict)

result = []

result_dict_keys = result_dict.keys()
for key in result_dict_keys:
    result.append({'name': key,
                'count': result_dict.get(key),
                'percent': round((result_dict.get(key) / result_dict.get('all')) * 100, 2)})

#print(result)

with open('data.json', 'w') as f:
    json.dump(result, f)