# Комментарии
# print(5)
"""
print(5)
print(5)
"""
# print(5)
# print(5)
# print(5)

# a = 5
# b = 5.89
# c = 'hell'

# Различные способы вывода
# print(a," - ", b, " - ", c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# Ввод данных
# print("Введите первое число: ")
# a = int(input())
# b = int(input("Введите второе число: "))
# print(a, " + ", b, " = ", a + b)

# Преобразование типов переменных
# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# Округление чисел
# a = 5.89956
# b = 6.556551
# print(round(a * b, 3))

# Итерации
# iter = 2
# iter += 2 # iter = iter + 2

# Условные операторы
# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это Маша!")
# elif username == "Марина":
#     print("Я так ждал Вас, Марина!")
# elif username == "Ильнар":
#     print("Ильнар - Топ!")
# else:
#     print("Привет, ", username)

#  Циклические операторы
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break  # в питоне не принято использовать
#     i = i + 1
# else:
#     print("Пожалуй хватит)")
# print(i)    

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток от деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может привышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


# for i in range(100, 0, -20): # Выводит числа от 100 до 0 с шагом -20
#     print(i)

# Работа со строками
# a = "qwerty"

# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

text = "СъЕШЬ еще этих МяГкИх французких булок"
# Срезы
print(text[:2]) # выводит "Съ"
print(text[2:9]) # выводит "ешь еще"
print(text[6:-18]) # выводит "еще этих мягких"
print(text[::6]) # выводит "свикакл"

print(len(text)) # Длина строки
print("еще" in text) # Определяет если "еще" в строке text
print(text.lower()) # Делает весь текст прописными
print(text.upper()) # Делает весь текст заглавными
print(text.replace("еще", "ЕЩЕ")) # меняет в строке text еще на ЕЩЕ