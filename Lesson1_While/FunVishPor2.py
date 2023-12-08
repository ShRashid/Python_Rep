# def hello(name):
#     return f"Hello, {name}"

# def bye(name):
#     return f"{name}, bye-bye"

# def create_two_phrases(funcs):
#     name = input("Введите ваше имя ")
#     res = ""
#     for func in funcs:
#         res += func(name) + "\n"
#     return res

# # print(create_phrase(hello))
# # print(create_phrase(bye))
# funcs = (hello, bye)
# print(create_two_phrases(funcs))

# def calc_power(degree):
#     def power(base):
#         return base ** degree
#     return power


# # print(calc_power(3) (2) )
# cube = calc_power(3)
# square = calc_power(2)
# print(cube(3))
# print(square(9))

# square_even = lambda x: x**2 if x%2 else 0
# print(square_even(9))

# calculator = {'+': lambda x,y: x + y, 
#               '-': lambda x,y: x - y, 
#               '*': lambda x,y: x * y, 
#               '/': lambda x,y: x / y}

# s = input("Введите арифметическое выражение ")
# x, op, y = s.split()
# print(f"Результат равен {calculator[op] (int(x),int(y)) }")

# s = input("Введите арифметическое выражение ")
# first, op, second = s.split()
# print(f"Результат равен {calculator[op] (int(first),int(second)) }")

# print(sp := [i for i in range(10)])
# print(list(map(lambda x: x**2, sp)))
# print(list(map(lambda x: x**2 if x%2 else 0, sp)))

# print(*filter(lambda x: x%2, sp))

# sp2 = ["Ваня", "Вася"]

# print(*zip(sp,sp2))

# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# square = [i,j if i != j for i,j in orbits ]
# print(square.index(max(square)))
# print(orbits[square.index(max(square))])

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
square = list(map(lambda item: item[0]*item[1] if item[0] != item[1] else 0, orbits))
print(orbits[square.index(max(square))])

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

def same_by(characteristic, objects):
    res = list(filter(characteristic, objects))
    return len(res) % len(objects) == 0


values = [1, 3, 5, 7]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")


