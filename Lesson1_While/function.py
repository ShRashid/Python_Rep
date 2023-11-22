import random 

def generate_num(low, high):
    num = random.randint(low, high)
    print(f"Было сформировано случайное число {num}")


def generate_num2(low, high):
    num = random.randint(low, high)
    return num


generate_num(0,15)
print(generate_num2(5,15))