# DZ 2 - 01. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.

a = float (input("Задайте вещественное число:  "))
# метод - умножает вещ. число на 10 за каждый знак после запятой и возвр. ИНТ
def floatToInt (x):
    while x%1!=0:
        x *=10
    return int(x)
# метод - сумма цифр INT числа
def sumOfdigits (x):
    if x>0:
        return int (x%10 + sumOfdigits(x/10))
    else:
        return 0

b = floatToInt (a)
print (sumOfdigits(b))
