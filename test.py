from pprint import pprint
from requests import get


url = 'https://api.hh.ru/vacancies'
params = {'text': 'python'}
res = get(url, params=params).json()
print(res['found'])
pprint(res['items'])


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

DOMAIN = 'https://api.hh.ru/'
url_vacancies = f'{DOMAIN}vacancies'
vakancy = 'python'

key_error = 0
index = 0

res = get(url, params=params).json()
it = res['items']
for item in it:
    count_all += 1
    snippet = str(item['snippet'])
    if snippet.find('SQL') != -1 or snippet.find('sql') != -1:
        count_SQL += 1
    if  snippet.find('pandas') != -1 or snippet.find('Pandas') != -1:
        count_pandas += 1
    if snippet.find('numphy') != -1 or snippet.find('Numphy') != -1:
        count_numphy += 1
    if snippet.find('PowerBI') != -1:
        count_PowerBI += 1
    if snippet.find('python') != -1 or snippet.find('Python') != -1:
        count_python += 1
    if snippet.find('swagger') != -1 or snippet.find('Swagger') != -1:
        count_swagger += 1
    if snippet.find('django') != -1 or snippet.find('Django') != -1:
        count_django += 1
    if snippet.find('fastapi') != -1 or snippet.find('Fastapi') != -1:
        count_fastapi += 1
    if snippet.find('tornado') != -1 or snippet.find('Tornado') != -1:
        count_tornado += 1
    if snippet.find('React') != -1 or snippet.find('react') != -1:
        count_React += 1
    if snippet.find('flask') != -1 or snippet.find('Flask') != -1:
        count_tornado += 1
    if snippet.find('sqlalchemy') != -1 or snippet.find('Sqlalchemy') != -1:
        count_React += 1

#print(res['found'])
#pprint(res['items'])

# while key_error == 0:
#
#     params = {
#         'text': vakancy,
#         # страница
#         'page': index,
#         'per_page': 100, # По 100 на странице
#         'only_with_salary': True, # Только с указанием зарплаты
#         'area': 1 # Только в Москве (а не в Москве никому пайтон разработчики и не нужны...)
#     }
#
#
#
#     index += 1
#     try:
#         result = requests.get(url_vacancies, params=params).json()
#         items = result['items']
#         for ind in range (100):
#             count_all += 1
#             first = items[ind]
#             snippet = str(first['snippet'])
#             if snippet.find('SQL') != -1 or snippet.find('sql') != -1:
#                 count_SQL += 1
#             if  snippet.find('pandas') != -1 or snippet.find('Pandas') != -1:
#                 count_pandas += 1
#             if snippet.find('numphy') != -1 or snippet.find('Numphy') != -1:
#                 count_numphy += 1
#             if snippet.find('PowerBI') != -1:
#                 count_PowerBI += 1
#             if snippet.find('python') != -1 or snippet.find('Python') != -1:
#                 count_python += 1
#             if snippet.find('swagger') != -1 or snippet.find('Swagger') != -1:
#                 count_swagger += 1
#             if snippet.find('django') != -1 or snippet.find('Django') != -1:
#                 count_django += 1
#             if snippet.find('fastapi') != -1 or snippet.find('Fastapi') != -1:
#                 count_fastapi += 1
#             if snippet.find('tornado') != -1 or snippet.find('Tornado') != -1:
#                 count_tornado += 1
#             if snippet.find('React') != -1 or snippet.find('react') != -1:
#                 count_React += 1
#             if snippet.find('flask') != -1 or snippet.find('Flask') != -1:
#                 count_tornado += 1
#             if snippet.find('sqlalchemy') != -1 or snippet.find('Sqlalchemy') != -1:
#                 count_React += 1
#     except KeyError:
#         key_error = 1
#     except IndexError:
#         key_error = 1
#
print(f'Всего = {count_all}')
print(f'SQL = {count_SQL}. В процентах - {(count_SQL / count_all)} %')
print(f'pandas = {count_pandas}. В процентах - {(count_pandas / count_all)} %')
print(f'numphy = {count_numphy}. В процентах - {(count_numphy / count_all)} %')
print(f'PowerBI = {count_PowerBI}. В процентах - {(count_PowerBI / count_all)} %')
print(f'python = {count_python}. В процентах - {(count_python / count_all)} %')
print(f'cswagger = {count_swagger}. В процентах - {(count_swagger / count_all)} %')
print(f'django = {count_django}. В процентах - {(count_django / count_all)} %')
print(f'fastapi = {count_fastapi}. В процентах - {(count_fastapi / count_all)} %')
print(f'tornado = {count_tornado}. В процентах - {(count_tornado / count_all)} %')
print(f'React = {count_React}. В процентах - {(count_React / count_all)} %')
print(f'flask = {count_flask}. В процентах - {(count_flask / count_all)} %')
print(f'sqlalchemy = {count_sqlalchemy}. В процентах - {(count_sqlalchemy / count_all)} %')