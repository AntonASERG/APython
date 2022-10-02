# ДЗ 3 - 02 .  Напишите программу, которая найдёт произведение пар чисел 
# списка (CСписок создаем как в предыдущем задании). Парой считаем первый 
# и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

a = int(input("введите число: "))


# Метод - выдает массив случайных чисел от 1 до Х
def randomArray (x):
    listA = []
    for i in range (x):
        listA.append(random.randint(1,10))
    return listA

# Метод - принимает массив и выдает массив произведений пар чисел
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def paraMultiplication (list):
    listPara = [] 
    b = len(list)//2 + len(list)%2 # переменная - длина вых. массива
    k = -1 # индекс второго элемента пары
    for i in range (b):
        listPara.append(list[i]*list[k])
        i+=1
        k-=1
    return listPara

listTotal = randomArray(a)

print(f"Массив = {listTotal}")
print(f"Произведение пар чисел  = {paraMultiplication(listTotal)}")
    