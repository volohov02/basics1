import requests
from bs4 import BeautifulSoup




url = 'http://garant-don.ru/index.php?m1=main'
response = requests.get(url)
str = response.text
# тут не задалось с кодировкой...
str = str.encode('ISO-8859-1').decode("utf-8")
soup = BeautifulSoup(str, 'html.parser')

print('Список новостей')
print('-'*40)

headers = soup.find_all('h3')
for head in headers:
    print(head.text)
print('-'*40)
print('Новостей на сайте: ', len(list(headers)))
print()

print('Список ссылок')
print('-'*40)
count_error = 0
count_in = 0
count_out = 0
for link in soup.find_all('a'):
    print(link.get('href'))
    if link.get('href') == None:
        print('----------------------- Это трындец - у вас битая ссылка! -----------------------')
        count_error += 1
    else:
        if link.get('href').find('http') == -1:
            count_in += 1
        else:
            count_out += 1

print('-'*40)
print('Всего ссылок на сайте: ', len(list(soup.find_all('a'))))
print('Из них наружу: ', count_out)
print('Из них внутри: ', count_in)
print('И косых ссылок: ', count_error)
print()

for image in soup.find_all('src'):
    print(image)