# Задача №13. Общее обсуждение
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# # ввод количества дней
# n = int(input("Введите общее количество рассматриваемых дней: "))

# # ввод среднесуточной температуры каждого дня
# temperatures = list(map(int, input("Введите среднесуточную температуру каждого дня через пробел: ").split()))

# # переменная для хранения текущей оттепели
# current_hot_streak = 0
# # переменная для хранения самой длинной оттепели
# max_hot_streak = 0

# # итерируемся по всем дням
# for temp in temperatures:
#     # если температура выше нуля, увеличиваем текущую оттепель
#     if temp > 0:
#         current_hot_streak += 1
#         # если текущая оттепель больше самой длинной, обновляем значение
#         if current_hot_streak > max_hot_streak:
#             max_hot_streak = current_hot_streak
#     else:
#         # если температура равна или ниже нуля, сбрасываем текущую оттепель
#         current_hot_streak = 0

# # выводим результат
# print("Самая длинная оттепель составила", max_hot_streak, "дней.")

import random

MIN_TEMPER, MAX_TEMPT = -50, 50

def create_list_days(n):
    days = []
    for i in range(n):
        days.append(
            random.randint(MIN_TEMPER, MAX_TEMPT)
        )
    print(*days)
    return days

def find_longest_thaw(temperatures):
    longest_thaw = 0
    current_thaw = 0

    for temperature in temperatures:
        if temperature > 0:
            current_thaw += 1
        else:
            current_thaw = 0

        if current_thaw > longest_thaw:
            longest_thaw = current_thaw

    return longest_thaw

n = int(input("Введите количество дней: "))
days = create_list_days(n)
print(find_longest_thaw(days))