# ДЗ 3 - 4. Напишите программу,
#  которая будет преобразовывать десятичное число в двоичное.


a = int(input("введите число в 10й системе: "))


# Метод - принимает целое число в 10й системе и возвр. строку
#  - число в двоичной системе

def stringBin (x):
    b = ''
 
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    return b
 
# Bin  - функция в Python

binA = bin(a)
print(f"В двоичной системе число {a} записывается как {stringBin (a)} или {binA}")


