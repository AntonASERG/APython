# DZ 4 -4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень 
# следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому 
# при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

pathWrite = r"C:\Users\User\Desktop\Python\APython\DZ4\file4_4.txt"

import random
k = int(input("Максимальная степень многочлена: - "))

dictM = {}
elemF = '' # элемент формулы
countF = '' # счетчик

for key in range (0,k):
    dictM[key] = random.randrange(-100, 101)
    if dictM[key] < 0:
        if key == 0:
            elemF = f'{dictM[0]}'
        else:
            elemF = f'{dictM[key]}x^{key}'
    else:
        if key == 0:
            elemF = f'+{dictM[0]}'
        else:
            elemF = f'+{dictM[key]}x^{key}'
    countF = elemF + countF 

endF = F'{countF} = 0' #  добавить }\{опку
endF = endF.replace("+", " + ").replace("-", " - ")
print (dictM)
print (endF)

try:
    with open (pathWrite, "w") as data:
        data.write(f'polynomial in grade {k}')
        data.write("\n")
        data.write(endF)
except:
    print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")



         
    





