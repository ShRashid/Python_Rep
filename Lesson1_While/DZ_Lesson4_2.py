# Черника

# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, 
# и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, 
# которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это 
# урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система 
# состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий 
# модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль 
# находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое 
# может собрать один собирающий модуль за один заход, находясь перед некоторым кустом 
# грядки.

# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го 
# куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое 
# может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования На входе: arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе: 19

# def maxBerries(arr):
#     n = len(arr)
    
#     # Создаем массив, где каждый элемент i будет хранить максимальное количество ягод,
#     # которые можно собрать, если начать с куста i
#     max_from = [0] * n
    
#     # Рассматриваем случаи, когда есть только один куст и два куста
#     max_from[0] = arr[0]
#     if n > 1:
#         max_from[1] = max(arr[0], arr[1])
    
#     # Для каждого куста считаем максимальное количество ягод, которое можно собрать,
#     # начиная с этого куста и двигаясь влево и вправо
#     for i in range(2, n):
#         max_from[i] = max(max_from[i-1], max_from[i-2] + arr[i])
        
#     # Возвращаем максимальное количество собранных ягод
#     return max_from[n-1]

# # Входные данные
# arr = [5, 8, 6, 4, 9, 2, 7, 3]

# # Вызов функции и вывод результата
# print(maxBerries(arr))  # Выведет: 19




# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# Урожай с куста
berryes = [5, 8, 6, 4, 9, 2, 7, 3] 
kust = len(berryes) # Количество кустов 
result = []
i = 0
sum = 0

# print(berryes)

while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"{result[-1]}")

# У вас есть список arr, представляющий урожайность каждого куста, 
# и переменная kust, представляющая количество кустов. Затем, используя 
# цикл while, вы проходите по каждому кусту, вычисляете сумму ягод с 
# текущего куста и двух соседних кустов, добавляете эту сумму в список result, 
# сортируете его и выводите наибольший элемент.
