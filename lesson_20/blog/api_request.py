import requests
import pprint

token = 'f0cf880b60644072c01734ab5cee8364034d10f7'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/vacancyes/', headers=headers)
#response = requests.get('http://127.0.0.1:8000/api/v0/vacancyes/')
pprint.pprint(response.json())

# response = requests.get('http://127.0.0.1:8000/api/v0/skills/', auth=('author', 'volohov02'))
#
# pprint.pprint(response.json())