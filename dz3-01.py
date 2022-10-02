# ДЗ 3 - 01 . Задайте рандомно список из чисел размером N, где N число с 
# клавиатуры. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

import random

a = int(input("введите число: "))


# Метод - выдает массив случайных чисел от 1 до Х
def randomArray (x):
    listA = []
    for i in range (x):
        listA.append(random.randint(1,10))
    return listA

# Метод - принимает массив и выдает сумму его нечетных (по индексу) элементов
def sumOfOddIndex (list):
    sumA = 0
    for i in range (1,len(list),2):
        sumA += list[i]
    return sumA

listTotal = randomArray(a)

print(f"Массив = {listTotal}")
print(f"Cумма элементов списка, стоящих на нечётной позиции = {sumOfOddIndex(listTotal)}")
    