# Бинарный поиск

def binary_search1(list, item) -> int:
    low = 0               # В переменных low и high храняться границы той части
    high = len(list) - 1  # списка, в которой выполняется поиск     

    while low <= high: # Пока эта часть не сократится до одного элемента ...
        mid = int((low + high) / 2) # ... проверяем средний элемент
        guess = list[mid]
        if guess == item: # Значение не найдено
            return mid
        if guess > item: # Много
            high = mid - 1
        else:            # Мало
            low = mid + 1
    return None          # Значение не существует 

my_list = [1, 3, 5, 7, 9]

print (binary_search1(my_list, 7))  # 1 Нумерация начинается с 0. Второй ячейке 
                                    # соотвествует индекс 1
print (binary_search1(my_list, -1)) # None в Питон означает "ничто". Это 
                                    # признак того, что элемент не найден
