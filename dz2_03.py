# DZ 2 - 03. Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму.

a = int (input("Задайте число N:  "))

# метод - принимает число N и выдает массив (1+1/n)^n
def arrayF (n):
    listA = []
    for i in range (1,n+1):# примечание - искл /0
        listA.append((1+1/i)**i)  
    return listA

# вывести массив
print (arrayF(a))
# вывести сумму элементов массива
print (sum(arrayF(a)))



