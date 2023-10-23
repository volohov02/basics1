from flask import Flask, g, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.vac = -1


# вывод (редеринг) главной страницы
@app.get('/index')
@app.get('/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        app.vac = request.form["text"]
        print(app.vac)
    return render_template('form.html')

@app.route('/result/', methods=['GET', 'POST'])
def result():
    name = app.vac if app.vac != -1 else 'Данных нет'
    headers = []
    news = []
    # print(name)
    url = 'http://garant-don.ru/index.php?m1=main'
    response = requests.get(url)
    str = response.text
    # тут не задалось с кодировкой...
    str = str.encode('ISO-8859-1').decode("utf-8")
    soup = BeautifulSoup(str, 'html.parser')
    if name == '1':
        news = []
        headers = soup.find_all('h3')
        header = f'Сейчас на сайте garant-don.ru доступны следующие новости (количество - {len(headers)}):'
        for head in headers:
            news.append(head.text)
    elif name == '2':
        news = []
        headers = soup.find_all('a')
        header = 'На главной странице сайта garant-don.ru обнаружены следующие ссылки:'
        for link in soup.find_all('a'):
            news.append(link.get('href'))
    else:
        news = []
        header = f'Нет данных'

    return render_template('result.html', news = news, header = header)

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)
