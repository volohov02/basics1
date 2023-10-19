import telebot
import requests
from bs4 import BeautifulSoup
import time
import os
from random import randint

TOKEN = '6491358972:AAHfXjH6zyFjV1VdhI1rTTFsW5o4L_-cPVY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, '/help - показывает описание команд \n /news - выдает количество новостей на сайте и заголовки первых трех новостей. \n /href - отправляет файл со списком ссылок \n /logo - показывает картинку логотипа. \n отправите стикер - получите в ответ рандомный стикер')

# Обработка команд
@bot.message_handler(commands=['news'])
def news(message):
    url = 'http://garant-don.ru/index.php?m1=main'
    response = requests.get(url)
    str = response.text
    # тут не задалось с кодировкой...
    str = str.encode('ISO-8859-1').decode("utf-8")
    soup = BeautifulSoup(str, 'html.parser')

    headers = soup.find_all('h3')


    bot.send_message(message.chat.id,f'Сейчас новостей на сайте: {len(list(headers))}')
    bot.send_message(message.chat.id, f'Первые три:')
    for head in headers[:3]:
        bot.send_message(message.chat.id, f'{head.text}')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    #print(message)
    choice = randint(0, 4)
    file_id = ' '
    if choice == 0:
        file_id = 'CAACAgIAAxkBAAMnZTFKyfLRSEzewen0C0BQKfZwIHQAAjMqAAIYZjhLyVrhiPIvMbkwBA'
    elif choice == 1:
        file_id = 'CAACAgIAAxkBAAMpZTFLBj1Hw5MNQvl9ecwVe-P95KwAAgQtAAIvihBLyBKl_QmgzTwwBA'
    elif choice == 2:
        file_id = 'CAACAgIAAxkBAAMrZTFLEPgZGjFX5SODaHAOHyfQLbMAApwyAAI3eRFLozw8yUnPUSMwBA'
    elif choice == 3:
        file_id = 'CAACAgIAAxkBAAMtZTFLFWRWuuSubWyP9Hw5LXMhbqwAAusuAALC5BFLAnyhnGuQZ18wBA'
    elif choice == 4:
        file_id = 'CAACAgIAAxkBAAMvZTFLHOoexiDw0dcx5FJxMFuiCr4AAqwzAAJx6DlL_mLwcP9jRRswBA'
    print(choice)
    print(file_id)

    bot.send_sticker(message.chat.id, file_id)

@bot.message_handler(commands=['logo'])
def get_file(message):
    with open('53327.jpg', 'rb') as data:
        bot.send_photo(message.chat.id, data)


@bot.message_handler(commands=['href'])
def get_file(message):
    url = 'http://garant-don.ru/index.php?m1=main'
    response = requests.get(url)
    str = response.text
    # тут не задалось с кодировкой...
    str = str.encode('ISO-8859-1').decode("utf-8")
    soup = BeautifulSoup(str, 'html.parser')
    count_error = 0
    count_in = 0
    count_out = 0
    FILE_NAME = 'href.txt'
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for link in soup.find_all('a'):
            str = link.get('href')
            f.write(f'{str} \n')
            if link.get('href') == None:
                f.write('----------------------- Это трындец - у вас битая ссылка! -----------------------\n')
                count_error += 1
            else:
                if link.get('href').find('http') == -1:
                    count_in += 1
                else:
                    count_out += 1
        str_len = len(list(soup.find_all('a')))
        f.write(f'Всего ссылок на сайте: {str_len} \n',)
        f.write(f'Из них наружу: {count_out} \n')
        f.write(f'Из них внутри: {count_in} \n')
        f.write(f'И косых ссылок: {count_error} \n')

    with open('href.txt', 'r', encoding='utf-8') as data:
        bot.send_document(message.chat.id, data)

bot.polling()