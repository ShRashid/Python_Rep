# print("Это наша первая программа")
# num1 = abs(int(input("Введите число: ")))
# print(f"Квадрат этого числа равен {num1 ** 2}")
# print(f"Целочисленное деление этого числа на 3 равно {num1 // 3}")
# print(f"Остаток от деления этого числа равно {num1 % 3}")
# print(f"Деление на 3 этого числа равно {num1 / 3}")
# if num1 > 0:
#     print("Вы ввели положительное число")
# elif num1 == 0:
#     print("Вы ввели 0")
# else:
#     print("Вы ввели отрицательное число")

# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output: 
# 2

# n = int(input("Введите скорость: "))
# m = int(input("Введите расстояние: "))

# c = m // n + 1 % (m % n + 1)

# print(f"Чтобы проехать {m} километров, нужно {c} дней")

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input("Кол-во учеников в 1-м классе: "))
# b = int(input("Кол-во учеников в 2-м классе: "))
# c = int(input("Кол-во учеников в 3-м классе: "))

# a1 = a // 2 + 1 % (a % 2 + 1)
# b1 = b // 2 + 1 % (b % 2 + 1)
# c1 = c // 2 + 1 % (c % 2 + 1)

# print(f"a1 = {a1}, b1 = {b1}, c1 = {c1}, кол-во парт - {a1 + b1 + c1}")

# Задача сложная.
# Посчитать сумму цифр любого целого или вещественного числа.
# Число вводит пользователь. Через строку решать нельзя.

# n = abs(float(input("Введите число: ")))
# sum = 0
# while n % 10 > 0: # находить числа после точки
#     n = n * 10
# while n > 0: # считаем сумму чисел числа
#     sum = sum + n % 10
#     n = n // 10
# print(sum)



# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input("Вагон в который сел Витя "))
# j = int(input("Вагон от головы поезда "))
# if i != j:
#     # p = i + j - 1
#     print(i + j - 1)
# else:
#     print("Без доп. информации это сделать не возможно!")

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

y = int(input("Введите год "))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("YES")
else:
    print("NO")
# print("YES" if y % 4 == 0 and y % 100 != 0 and y % 400 == 0 else "NO")

# Задача:
# Посчитать количество цифр введенного числа

# n = abs(float(input("Введите число: ")))
# count = 0
# sum = 0
# while n % 10 > 0: # находить числа после точки
#     n = n * 10
# while n > 0: # считаем сумму чисел числа
#     # sum = sum + n % 10
#     count += 1
#     n = n // 10
# print(count-1)

