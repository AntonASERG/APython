# DZ 4 -1 Вычислить число π c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# разделить строку на целую и дробную части
d = str(input('Введите число D в формате 0.1:   ')).split(".")
# print (d) 

# определить количество после запятой
countAfterPoint = int (len(d[1]))
print(f'количество знаков после запятой: {countAfterPoint}')

# вывести число пи с округлением D
import math
a = round (math.pi,countAfterPoint)
print (f"π =  {a}")


