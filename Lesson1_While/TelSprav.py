# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import json


phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                           'birthday': "05.05.1990", 'email': "12@ya.ru"},
             "Дядя Вася": {'phones' : [54654541]}
             }

def save():
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))
    print("")

def load():
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        telephone = json.load(doc)
    print("")
    return telephone


print(phonebook['Дядя Ваня'])
# print(phonebook['Дядя Ваня']['phones'])
# print(phonebook['Дядя Ваня']['phones'][0])

for name, values in phonebook.items():
    print(name, values)
print("Открыт телефонный справочник")

try:
    load()
except:
    phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                               'birthday': "05.05.1990", 'email': "12@ya.ru"},
                 "Дядя Вася": {'phones': [54654541]}
                 }

while True:
    command = input("Введите команду ")
    if (command == "/exit"):
        break
    elif command == "/load":
        load()
    elif command == "/save":
        save()
        print("Новая запись добавлена")
    elif command == "/all":
        print("Текущий телефонный список")
        print(phonebook)
    elif command == "/add":
        name = input("Введите имя: ")
        email = input("Введите EMAIL: ")
        phone = input("Введите номера телефонов через пробел: ").split()
        phonebook.
        if phone != "":
            phonebook[name] = phone
        else:
            continue
    else:
        print("Вы ввели не верную комманду, изучите мануал!")