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


def fibs(num):
    nums_pos = [0, 1]
    nums_neg = [0, 1]
    for i in range(num - 1):
        nums_pos.append(nums_pos[i] + nums_pos[i + 1])
        nums_neg.append(nums_neg[i] - nums_neg[i + 1])
    return (nums_neg[:1:-1] + nums_pos)

print(fibs(8))


