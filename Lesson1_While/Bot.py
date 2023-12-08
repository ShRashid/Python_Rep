from random import *
import json

films=[]

# Запись фильмотеки в файл films.json
def save():
    with open("films.json", "w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json") 

# Загрузка фильмотеки из файла films.json
def load():
    with open("films.json", "r",encoding="utf-8") as fh:
        films = json.load(fh)
    print("Наша фильмотека была успешно загружена из файле films.json")

# Если файл со списком фильмов не существует формируется список по умолчанию
try:
    with open("films.json", "r",encoding="utf-8") as fh:
        films = json.load(fh)
    print("Наша фильмотека была успешно загружена из файле films.json")
except:    
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара")

while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот - фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот завершил работу. Заходите еще, будем рады")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f=input("Введите название фильма: ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию")
    elif command == "/help":
        print("Здесь какой-то мануал")
    elif command == "/help":
        print("Здесь какой-то мануал")
    elif command == "/delete":
        f=input("Введите название фильма который хотите удалить: ")
        '''
        if f in films:
            films.remove(f)
            print("Фильм был успешно удален в коллекцию")
        else:
            print("Фильм не найден в коллекции")
        '''
        try:
            films.remove(f)
            print("Фильм был успешно удален в коллекцию")
        except:
            print("Фильм не найден в коллекции")
    elif command == "/random":
        # rnd = randint(0,len(films-1))
        # print("Слепой жребий показал вам фильм - " + films[rnd])
        # choise - Работает с структурами типа списков, выдает случаное значение 
        # из списка, тоже из билиотеки random
        print("Слепой жребий показал вам фильм - " + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда. Росьба изучить мануал через /help")
