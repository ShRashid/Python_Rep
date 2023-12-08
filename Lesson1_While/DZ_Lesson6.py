# Элементы из заданного диапазона
# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного 
# максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел 
# min_number, max_number.
# Пример
# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

# def index_d(List_1, min, max):
#     count = 0
#     for i in list_1:
#         if i >= min and i <= max:
#             print(str(count))
#         count += 1
  
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# index_d(list_1,min_number,max_number)


# Арифметическая прогрессия
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 ,
# разность d и количество элементов n будет задано автоматически. Формула для 
# получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример
# На входе:
# a1 = 2
# d = 3
# n = 4
# На выходе:
# 2
# 5
# 8
# 11

# def arifm_progression(a1,d,n):
#     for i in range(1,n+1):
#         print(a1 + (i-1) * d)

# a1 = 2
# d = 3
# n = 4
# arifm_progression(a1,d,n)

# Задача FOOTBALL необязательная

# Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех 
# матчей.
# ​
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# ​
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# ​
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# ​
# Конкретный пример ввода-вывода приведён ниже.
# ​
# Порядок вывода команд произвольный.
# ​
# Пример входа:
# ​
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# ​
# Выход будет:
# ​
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

def get_team_points(results, team):
    wins = results[team].count("W")
    draws = results[team].count("D")
    losses = results[team].count("L")
    total_points = 3 * wins + draws
    return (wins, draws, losses, total_points)


n = int(input("Введите количество завершенных игр: "))
results = {}
for i in range(n):
    game = input("Введите результаты игры: ").split(";")
    team1, score1, team2, score2 = game
    if score1 > score2:
        results[team1] = results.get(team1, "") + "W"
        results[team2] = results.get(team2, "") + "L"
    elif score1 < score2:
        results[team2] = results.get(team2, "") + "W"
        results[team1] = results.get(team1, "") + "L"
    else:
        results[team1] = results.get(team1, "") + "D"
        results[team2] = results.get(team2, "") + "D"

print("Команда: Всего игр Побед Ничьих Поражений Всего очков")
for team in results.keys():
    wins, draws, losses, total_points = get_team_points(results, team)
    total_games = wins + draws + losses
    print(f"{team}: {total_games} {wins} {draws} {losses} {total_points}")

