# ДЗ 3 - 03. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как
#  минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

a = int(input("введите длинну массива: "))


# Метод - принимает длину массива и выдает массив случайных вещественных чисел 
def randomFloatArray (x):
    listA = []
    for i in range (x):
    # *10 (таким образом задаем диапазон от 0.00 до 9.99)
        listA.append(random.random()*10)
    # цикл для округления
    for i in range (len(listA)):
        listA[i] = round(listA[i],2)
        i+=1
    return listA

#Метод , который найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.(за искл 0)
def floatO_Max_Min (list):
    maxL = list [0]%1
    minL = list [0]%1
    sumO = 0
    for i in range (len(list)):
        if list[i]%1 == 0:
            maxL = maxL 
        elif list[i]%1 < minL:
            minL = list[i]%1
        elif list [i]%1 > maxL:
            maxL = list[i]%1
        i+=1
    
    sumO = round((maxL -minL),2)
    return sumO

    
listTotal = randomFloatArray(a)
print(f"Массив = {listTotal}")
print (f"разницa между максимальным и минимальным значением дробной части элементов = {floatO_Max_Min(listTotal)}")

    