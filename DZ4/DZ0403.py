# DZ 4 -3 Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов  исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

strA = input("введите последовательность цифр:   ")

# метод COUNTER - принимает массив (строку)
#  и возвращает словарь (значение: количество повторов)
from collections import Counter
from xml.etree import ElementInclude

dictIn = Counter(strA)
dictOut = {}
# array = [] - альтернативный вариант dictOut = {}
for key in dictIn:
    if dictIn[key] == 1:
        dictOut[key] = 1 # добавлять новые элементы в словарь Словарь [ключ]= знач
        # array.append(key)
print (dictOut.keys())   # вывести ключи
# print (array)




         
    





