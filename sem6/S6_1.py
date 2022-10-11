# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел..



# метод - раскладывает число INT на простые множители (LIST [])
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

#  метод - принимает два  [] размножения на прост. множители А и В и выдает их НОК
def nokAB (factA, factB):
    nok = 1

    # цикл найти элемент в одном списке и удалить в другом
    for element in factA:
        if element in factB:
            factB.remove(element)
    # сложить два массива
    buffer = factA+factB
    #  перемножить элементы массива
    for elem in buffer:
        nok *= elem
    return nok


a = int(input("a =  "))
b = int(input("b =  "))

factA = factor(a)
factB = factor(b)

nok = (nokAB(factA,factB))

print (factA)
print (factB)
print (nok)