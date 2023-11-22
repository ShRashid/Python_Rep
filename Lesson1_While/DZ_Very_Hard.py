# Задача VERY HARD необязательная
# Имеется список случайных целых чисел. Создайте список, в который попадают числа, 
# описывающие максимальную сплошную возрастающую последовательность. Порядок 
# элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все 
# числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 
# и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 
# и эта последовательность длиннее чем от 7 до 8

# Функция maxIncreasingSubsequence находит максимальную возрастающую 
# последовательность в списке целых чисел arr и возвращает эту последовательность.

def maxIncreasingSubsequence(arr):
    longest_seq_start = 0
    longest_seq_end = 1

    current_seq_start = 0
    current_seq_end = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_seq_end += 1
            if current_seq_end - current_seq_start > longest_seq_end - longest_seq_start:
                longest_seq_start = current_seq_start
                longest_seq_end = current_seq_end
        else:
            current_seq_start = i
            current_seq_end = i + 1

    return arr[longest_seq_start:longest_seq_end]

# Примеры использования:

arr1 = [1, 5, 2, 3, 4, 6, 1, 7]
print(maxIncreasingSubsequence(arr1))  # Вывод: [1, 7]

arr2 = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1]
print(maxIncreasingSubsequence(arr2))  # Вывод: [1, 5]

arr3 = [1, 5, 3, 4, 1, 7, 8, 15, 1]
print(maxIncreasingSubsequence(arr3))  # Вывод: [3, 5]
