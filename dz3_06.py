# Задача 3-6. Реализуйте алгоритм задания случайных чисел без использования
#  встроенного генератора псевдослучайных чисел.
# сделал по колхозному, зато в виде игры)

a = int (input("какую цифру я загадал:  "))

import datetime

now = datetime.datetime.now()
strNow = str (now)
b = int (strNow[-3])

if a == b:
    print (f"Угадал")
else:
    print (f"Нет. я загадал : {strNow[-3]}")


# для наглядности
print(strNow)
