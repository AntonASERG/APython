#  ДЗ 3 - 05. Задайте число - размер списка. Составьте список чисел Фибоначчи,
#   в том числе для отрицательных индексов.
# *Пример:*
# - для а = 8 список будет выглядеть 
# так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


a = int(input("введите длинну массива: "))


# Метод ФИБОНАЧИ!!! 
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

listF = []
for i in range (1,a+1):
    listF.append(fib(i))


# Метод НЕГАФИБОНАЧИ!!!
def negafib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negafib(n+2) - negafib(n+1)

listNF = []
for i in range (-a,0):
    listNF.append(negafib(i))


# Фибоначи для ноля...наверное)
listO = [0,]

# Соединяем - 0 +
totalList = listNF + listO + listF
print(totalList)