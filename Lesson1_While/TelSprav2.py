import json

def load_data():
    try:
        with open('phonebook.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open('phonebook.json', 'w') as file:
        json.dump(data, file, indent=4)

def view_contacts(data):
    for name, number in data.items():
        print(f'{name}: {number}')

def add_contact(data, name, number):
    data[name] = number
    save_data(data)
    print('Контакт успешно добавлен')

def delete_contact(data, name):
    if name in data:
        del data[name]
        save_data(data)
        print('Контакт успешно удален')
    else:
        print('Такого контакта нет в справочнике')

def search_contact(data, name):
    if name in data:
        print(f'{name}: {data[name]}')
    else:
        print('Такого контакта нет в справочнике')

def modify_contact(data, name, new_number):
    if name in data:
        data[name] = new_number
        save_data(data)
        print('Контакт успешно изменен')
    else:
        print('Такого контакта нет в справочнике')


data = load_data()
while True:
    print('1. Просмотр справочника')
    print('2. Добавить контакт')
    print('3. Удалить контакт')
    print('4. Поиск контакта')
    print('5. Изменить контакт')
    print('6. Выйти')
    choice = input('Выберите действие: ')

    if choice == '1':
        view_contacts(data)
    elif choice == '2':
        name = input('Введите имя контакта: ')
        number = input('Введите номер телефона: ')
        add_contact(data, name, number)
    elif choice == '3':
        name = input('Введите имя контакта, которого нужно удалить: ')
        delete_contact(data, name)
    elif choice == '4':
        name = input('Введите имя контакта для поиска: ')
        search_contact(data, name)
    elif choice == '5':
        name = input('Введите имя контакта для изменения: ')
        new_number = input('Введите новый номер телефона: ')
        modify_contact(data, name, new_number)
    elif choice == '6':
        break
    else:
        print('Неверный выбор, попробуйте снова')

