# 4-2 уравнение AX**2+BX+C = 0

pathRead = r"file.txt"
pathWrite = r"file2.txt" # r  чтобы в названия не растознались элементы кода

# команда - ПОПРОБУЙ СДЕЛАЙ ЭТО:
try:
    with open(pathRead, "r") as data:  # оптимальный вариант
        file = data.read().split(" ")
except:
    print("не найден")

print (file)
listInt = []

for elem in file: 
     i = 0
     while elem[0+i].isdigit():# пока  позиция в элементе цифра?
            listInt.append(elem[0+i])
            i+=1
print (listInt)



a = int (listInt[0])
b = int (listInt[1])
c = int (listInt[2])

result = ''

# МЕТОД Формула дискриминанта
def discriminant (a,b,c):
    
    import math
    
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        result = f"x1 = {x1} \n x2 = {x2}"
    elif discr == 0:
        x = -b / (2 * a)
        result = f"x1 = x2 = {x}"
    else:
        result = "Корней нет"
    print (result)
    return result
    

try:
    with open (pathWrite, "w") as data:
        data.write(discriminant(a,b,c))
        
except:
    print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")