# посчитать сумму всех натуральных чисел от 1 до n, 
# где n вводится пользователем

# Функция принимает значение n типа int и возвращает значение типа int
# def summa_cycle(n: int) -> int:
#     res = 0
#     while True:
#         if n == 0:
#             break
#         res += n
#         n -= 1
#     return res

# def summa_rec(n: int) -> int:
#     if n == 0:
#         return 0
#     return n + summa_rec(n-1)

# # 1. погружение
# # summa_rec(4) = (4 + (3 + (2 + (1 + 0))))
# # 2. всплытие
# # (4 + (3 + (2 + (1 + 0)))) = 4 + (3 + 3) = 10

# n = int(input("Введите натуральное число "))
# print(summa_cycle(n))
# print(summa_rec(n))

# Посчитать количество сотрудников коропрации во всех подразделениях

# def get_count_all(sp: list) -> int:
#     res = 0
#     for item in sp:
#         if isinstance(item, list):
#             res += get_count_all(item)
#         else:
#             res += item
#     return res

# count_angola = 18
# count_new_york = [20, [10, 7]]
# count_chicago = 15
# count_usa = [count_new_york,count_chicago ]
# count_all = [count_angola, count_usa]
# # [18, [[20, [10, 7]], 15]]
# print(count_all)
# print(get_count_all(count_all))

# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# Решение в группе
# def fi(n, memo={}):
#     if n in [1, 2]:
#         return 1
#     if n not in memo:
#         memo[n] = fi(n - 1, memo) + fi(n - 2, memo)
#     return memo[n]

# print(fi(7, memo={}))

# Решение ИИ
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))

# N = 7
# result = fibonacci(N)
# print(result)  # Output: 13


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def mark(list, index, max_num):
#     if index == len(list):
#         return
#     if list[index] == max_num:
#         list[index] = min(list)
#     return mark(list, index + 1, max_num)

# lst = [1, 4, 4, 3, 3]
# max_num = max(lst)
# mark(lst, 0, max_num)
# print(lst)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# Решение ИИ
# def is_prime(n, divisor=2):
#     if n < 2:
#         return "no"
#     elif n == 2:
#         return "yes"
#     elif n % divisor == 0:
#         return "no"
#     elif divisor * divisor > n:
#         return "yes"
#     else:
#         return is_prime(n, divisor + 1)

# number = 3
# print(is_prime(number))  # Output: yes

# Решение в группе
# def simple_num(num, index=None):
#     if index is None:
#         index = num - 1
#     if index == 1:
#         return 'yes'
#     if num % index == 0:
#         return 'no'

#     return simple_num(num, index - 1)

# print(simple_num(5))

# Быстрая сортировка 
# ● 1-е повторение рекурсии:
#   ○ array = [10, 5, 2, 3]
#   ○ pivot = 10
#   ○ less = [5, 2, 3]
#   ○ greater = []
#   ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
#   ○ array = [5, 2, 3]
#   ○ pivot = 5
#   ○ less = [2, 3]
#   ○ greater = []
#   ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
#   здесь помимо вызова рекурсии добавляется список [10]
# ● 3-е повторение рекурсии:
#   ○ array = [2, 3]
#   ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
# образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 2, 3]))

# Сортировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)

# Задача 1 Напишите рекурсивную программу вычисления арифметического 
# выражения заданного строкой. Используйте операции +,-,/,*. приоритет 
# операций стандартный.

# *Пример:* 
# 2+2-8*2 => -12; 
# 1+2*3/6 => 2; 
# 1-2*3 => -5;

def calculate(expression):
    if '+' in expression:
        index = expression.index('+')
        return calculate(expression[:index]) + calculate(expression[index+1:])
    elif '-' in expression:
        index = expression.index('-')
        return calculate(expression[:index]) - calculate(expression[index+1:])
    elif '*' in expression:
        index = expression.index('*')
        return calculate(expression[:index]) * calculate(expression[index+1:])
    elif '/' in expression:
        index = expression.index('/')
        return calculate(expression[:index]) / calculate(expression[index+1:])
    else:
        return float(expression)

# Примеры использования
print(calculate("2+2-8*2")) # -12
print(calculate("1+2*3/6")) # 2
print(calculate("1-2*3")) # -5