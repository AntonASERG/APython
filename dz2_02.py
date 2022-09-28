# DZ 2 - 02. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) 

a = int (input("Задайте число N:  "))

# метод - принимает число N и выдает массив произведений чисел от 1 до N.
def arrayDigitsMltiplier (n):
    listA = []
# буфферный накопитель
    buf = 1
    for i in range (1,n+1):
        listA.append(i*buf)
        buf*=i
    return listA

print (arrayDigitsMltiplier(a))



