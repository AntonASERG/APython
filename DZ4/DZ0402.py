# DZ 4 -2 Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N.

n = int (input("Введите число N:  "))

# метод - раскладывает число на простые множители
def factor(n):
    listN = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            listN.append(d)
            n = n//d
        else:
            d += 1
    if n > 1:
        listN.append(n)
    return listN

print (f"Простые множители: {factor(n)}")


