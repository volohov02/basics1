from flask import Flask, g, render_template, request
import requests
from bs4 import BeautifulSoup
from sqlite3 import connect
import sqlite3

app = Flask(__name__)
app.vac = -1

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id}) {self.name}'

class Href(Base):
    __tablename__ = 'href'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id} {self.name}'


# Создание таблицы
Base.metadata.create_all(engine)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

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
        idi = 0
        for head in headers:
            news.append(head.text)
            new = head.text
            new_str = News(new)
            session = Session()
            session.add(new_str)
            session.commit()

    elif name == '2':
        news = []
        headers = soup.find_all('a')
        header = 'На главной странице сайта garant-don.ru обнаружены следующие ссылки:'
        for link in soup.find_all('a'):
            news.append(link.get('href'))
            new = link.get('href')

            new_str = Href(new)
            session = Session()
            session.add(new_str)
            session.commit()

    else:
        news = []
        header = f'Нет данных'

    return render_template('result.html', news = news, header = header)

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)





