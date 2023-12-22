import telebot
from random import *
import json
import requests

films = []
films_try = False

# Запись фильмотеки в файл films.json
def save():
    with open("films.json", "w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))

# Загрузка фильмотеки из файла films.json
def load():
    with open("films.json", "r",encoding="utf-8") as fh:
        films = json.load(fh)
        
try:
    with open("films.json", "r",encoding="utf-8") as fh:
        films = json.load(fh)
    films_try = True       
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара") 
     
# t.me/GB_Test001_bot - адрес телеграмм бота
API_TOKEN = '6815550887:AAFIcrat6cIPGo1ETA0T8GIkDBuWEU6RhG8' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    if films_try == False:
        bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию")
    else:
        bot.send_message(message.chat.id,"Наша фильмотека была успешно загружена из файле films.json")
        
    
@bot.message_handler(commands=['stop'])
def stop_all(message):
    save()
    bot.send_message(message.chat.id,"Бот завершил работу. Заходите еще, будем рады")
    
@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Вот список фильмов:")        
        bot.send_message(message.chat.id,", ".join(films))   
    except:
        bot.send_message(message.chat.id,"Фильмотека пустая!")

@bot.message_handler(commands=['add'])  
def add_name_film(message):     
    f = message.text.split()[1:]
    films.append(" ".join(f))
    save_all(message)
    bot.send_message(message.chat.id,"Фильм был успешно добавлен в коллекцию")
    
@bot.message_handler(commands=['help']) 
def help_bot(message):
    bot.send_message(message.chat.id,"Ниже представлены команды бота:")
    bot.send_message(message.chat.id,"/start - Запуск бота")
    bot.send_message(message.chat.id,"/stop - Завершение работы бота с сохранением")
    bot.send_message(message.chat.id,"/all - Выводит список фильмов фильмотеки")
    bot.send_message(message.chat.id,"/add <Название фильма> - Добавляет фильм в фильмотеку")
    bot.send_message(message.chat.id,"/help - Выводит данный справочник")
    bot.send_message(message.chat.id,"/save - Записывает фильмотеку в файл films.json")
    bot.send_message(message.chat.id,"/delete <Название фильма> - Удаляет указанный фильм")
    bot.send_message(message.chat.id,"/rnd - Выводит случайный фильм из фильмотеки")

@bot.message_handler(commands=['save'])
def save_all(message):
    save()
    bot.send_message(message.chat.id,"Наша фильмотека была успешно сохранена в файле films.json")
 
@bot.message_handler(commands=['delete'])
def delete_film(message):
    f = message.text.split()[1:]
    try:
        films.remove(" ".join(f))
        bot.send_message(message.chat.id,"Фильм был успешно удален из коллекции")
    except:
        bot.send_message(message.chat.id,"Фильм не найден в коллекции")
      
@bot.message_handler(commands=['rnd'])
def random_film(message):
    bot.send_message(message.chat.id,"Слепой жребий показал вам фильм - " + choice(films))
          
bot.polling()
