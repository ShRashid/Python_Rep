import telebot
from random import *
import json
import requests

films=[]
data=""

API_URL = 'https://7012.deeppavlov.ai/model'

# t.me/GB_Test001_bot - адрес телеграмм бота
API_TOKEN = '6815550887:AAFIcrat6cIPGo1ETA0T8GIkDBuWEU6RhG8' 
bot = telebot.TeleBot(API_TOKEN)

def view_help(message):
    bot.send_message(message.chat.id,'/view - Просмотр справочника')
    bot.send_message(message.chat.id,'/add - Добавить контакт (Пример: /add Имя Телефон)')
    bot.send_message(message.chat.id,'/del -  Удалить контакт (Пример: /del )')
    bot.send_message(message.chat.id,'/search - Поиск контакта')
    bot.send_message(message.chat.id,'/ren -  Изменить контакт')
    bot.send_message(message.chat.id,'/save -  Записать все контакты')
    bot.send_message(message.chat.id,'/stop Выйти')    


@bot.message_handler(commands=['start'])
# def start_message(message):
def load_data(message):
    view_help(message)
    try:
        with open('phonebook.json', 'r') as file:
            data = json.load(file)
            bot.send_message(message.chat.id,"Справочник загружен")
    except FileNotFoundError:
        data = {}
        bot.send_message(message.chat.id,"Справочник пока пуст, можно приступать к заполнению")
    
 
@bot.message_handler(commands=['add'])  
def add_contact(message):
    name = message.text.split()[1:2]
    number = message.text.split()[2:]
    data[name] = number
    save_data(message)
    bot.send_message(message.chat.id,'Контакт успешно добавлен')

@bot.message_handler(commands=['save'])    
def save_data(message):
    with open('phonebook.json', 'w') as file:
        json.dump(data, file, indent=4)
    bot.send_message(message.chat.id,"Справочник успешно записан") 
    
  


# @bot.message_handler(commands=['all'])
# def show_all(message):
#     try:
#         bot.send_message(message.chat.id,"Вот список фильмов:")
#         bot.send_message(message.chat.id,", ".join(films))
#     except:
#         bot.send_message(message.chat.id,"Фильмотека то пустая!")

# @bot.message_handler(commands=['save'])
# def save_all(message):
#     with open("films.json", "w",encoding="utf-8") as fh:
#         fh.write(json.dumps(films,ensure_ascii=False))
#     bot.send_message(message.chat.id,"Наша фильмотека была успешно сохранена в файле films.json")
    
# @bot.message_handler(commands=['Wiki']) 
# def wiki(message):
#     quest = message.text.split()[1:]
#     qq=" ".join(quest)
#     data = { 'question_raw': [qq]}
#     try:
#         res = requests.post(API_URL,json=data,verify=False).json()
#         bot.send_message(message.chat.id, res)
#     except:
#         bot.send_message(message.chat.id,"Что-то я ничего не нашел :-(")
        
# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     if "дела" in message.text.lower():
#         bot.send_message(message.chat.id,"Дела у меня хорошо. Как сам?")
        
bot.polling()