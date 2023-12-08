sp = []
sp = [5,3,6,7,True,False, "Hello", 9.99," world "]

t = tuple(sp)

# t[0] = 123

# print(len(sp))
# print(10 in sp) 
# print(5 in set(sp))
# sp.extend( [777,888])
# sp.insert(0, 123)
# # print(sp)
# del sp[0]
# a = sp.pop()
# sp.remove(True)
# print(sp, a)
# print(sp[1:4])
# s = {1,1,1,1,2,2,2,7,7,7}
# print(s)
# d = {"Ваня": 4564654, "Вася": 56123131}
# d["Виталий"] = 77777
# print(d.keys())
# print(d.values())
# for key, value in d.items():
#     print(f"{key} - {value}")

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(list(set(my_list))))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# def shift_sequence(arr, k):
#     n = len(arr)
#     k = k % n  # убедимся, что сдвиг меньше, чем длина последовательности
    
#     arr[:] = arr[-k:] + arr[:-k]  # выполняем циклический сдвиг вправо

# arr = [1, 2, 3, 4, 5]
# k = 3
# shift_sequence(arr, k)
# print(arr)  # [4, 5, 1, 2, 3]

# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     left_list = input_list[:-pivot]
#     right_list = input_list[-pivot:]
#     moved_list = right_list + left_list 
#     return moved_list

# input_list = [1, 2, 3, 4, 5]
# k = 3

# print(move(input_list, k))

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# 1
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#         {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# unique_values = set(val for dic in data for val in dic.values())
# print(unique_values)  # вывод уникальных значений

# 2
# arr = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007"}]

# unique_values = set()

# for dictionary in arr:
#     for value in dictionary.values():
#         unique_values.add(value.strip())  

# print(unique_values)

# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 
# 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# def fibs(num):
#     nums_pos = [0, 1]
#     nums_neg = [0, 1]
#     for i in range(num - 1):
#         nums_pos.append(nums_pos[i] + nums_pos[i + 1])
#         nums_neg.append(nums_neg[i] - nums_neg[i + 1])
#     return (nums_neg[:1:-1] + nums_pos)

# print(fibs(8))


# Использование обхода ошибок

# # def print_sp(sp: list):
#     if not isinstance(sp, list):
#         print("Нужен именно список!")
#         return
#         # raise ValueError("Нужен именно список!")
#     for i,v in enumerate(sp):
#         print(f"{i=} - {v=}")



# sp = [5, 8, 9, True, 'Hello']
# s = "Hello"
# print_sp(s)

# Обход ошибок
# try:
#     print_sp(sp)
#     print_sp(s)
# except ValueError as e:
#     print(e)


# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# input_string = input("Input: ")
# input_string = "a a a b c a a d c d d"
# chars = input_string.split()

# char_count = {}
# for char in chars:
#     if char in char_count:
#         char_count[char] += 1
#         print(char + "_" + str(char_count[char]), end=" ")
#     else:
#         char_count[char] = 1
#         print(char, end=" ")

# b = 'a a a b c a a d c d d'
# a = ''
# b = b.split(' ')
# for i in b:
#     count_1 = a.count(i)
#     if count_1 == 0:
#         a += i+' '
#     else:
#         a += i+'_'+str(count_1)+' '
# print(a.strip())

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# string = ("She sells sea shells on the sea shore The shells"
#           " that she sells are sea shells I'm sure.So if"
#           " she sells sea shells on the sea shore I'm sure"
#           " that the shells are sea shore shells")
# print(len(set(string.replace(".", " ").lower().split())))

# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, 
# где все коэффициенты случайные от -10 до 10.
# ​
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

# import random
# k = int(input("Введите степень многочлена: "))
# res = ""
# coefficients = [random.randint(-10, 10) for _ in range(k+1)]
# mmm = ' + '.join([f'{coefficients[i]}x^{i}' for i in range(k + 1)])

# print(f"многочлен степени {k} от -10 до 10: {mmm}")

# pr = '22*4+3'
# sp=[]
# res = ""
# for symb in pr:
#     if not (res + symb).isdigit():
#         sp.append(res)
#         res = ""
#         sp.append(symb)
#     else:
#         res += symb
# sp.append(res)
    
# print(sp) # ['22','*','4','+','3']

from random import randint


def create_list(lower, upper, count):
    res = []
    for _ in range(count):
        res.append(randint(lower, upper))
    return res



# print(create_list(-5,10,5))
# print( sp := [randint(-5, 10)  for _ in range (5) ] )
sp = [i for i in range(10)]
print(sp)

print([i**2 for i in sp])
print([i**2  for i in sp if i%2 ])
print([i**2 if i%2 else 0 for i in sp ])
print(sum([i**2 if i%2 else 0 for i in sp ]))

print({i: chr(i) for i in range (5) })

