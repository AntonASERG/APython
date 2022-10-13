# DZ 2 - 03. Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму.

# LIST COMPREHENSON
a = int (input("Задайте число N:  "))


# LIST COMPREHENSON
listA = [((1+1/i)**i) for i in range (1,a+1)]
print (sum(listA))

# # LAMBDA
listB = list(range (1,a+1))
listB = list (map(lambda x :(1+1/x)**x, listB))
print (sum(listB))




# ==================================================================================
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



