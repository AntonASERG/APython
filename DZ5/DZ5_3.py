# DZ5-3. Создайте программу для игры в 'Крестики-нолики'.
#  конфигурация для игры с калькулятора :) (NumPad)

mas1 = [['_', '1', '2', '3'], ['1', '_', '_', '_'], ['2', '_', '_', '_'],['3', '_', '_', '_']]

# метод принимает 2д массив и выводит ео на печать в формате XY (таблицей)
def printXY (mas):
    for i in range(0, len(mas)):
        for i2 in range(0, len(mas[i])):
            print(mas[i][i2], end='|')
        print()

printXY(mas1)

ok = False
while ok == False:
    x = int (input("x - "))
    y = int (input("y - "))
    mas1[y][x] = input ('+ или 0:  ')
    printXY(mas1)

#  ПРОБОВАЛ ЧЕРЕЗ  цикл for i in range (3) b т.п. но постоянно ошибки выскакивали
    if mas1[1][1] == mas1[1][2] == mas1[1][3] == "+" :
        ok = True
    elif mas1[1][1] == mas1[1][2] == mas1[1][3] == "0" :
        ok = True

    elif mas1[2][1] == mas1[2][2] == mas1[2][3] == "+" :
        ok = True
    elif mas1[2][1] == mas1[2][2] == mas1[2][3] == "0" :
        ok = True

    elif mas1[3][1] == mas1[3][2] == mas1[3][3] == "+" :
        ok = True
    elif mas1[3][1] == mas1[3][2] == mas1[3][3] == "0" :
        ok = True

    elif mas1[1][1] == mas1[2][1] == mas1[3][1]== "+":
        ok = True
    elif mas1[1][1] == mas1[2][1] == mas1[3][1]== "0":
        ok = True

    elif mas1[1][2] == mas1[2][2] == mas1[3][2]== "+":
        ok = True
    elif mas1[1][2] == mas1[2][2] == mas1[3][2]== "0":
        ok = True

    elif mas1[1][3] == mas1[2][3] == mas1[3][3]== "+":
        ok = True
    elif mas1[1][3] == mas1[2][3] == mas1[3][3]== "0":
        ok = True

    elif mas1[1][1] == mas1[2][2] == mas1[3][3]== "+":
        ok = True
    elif mas1[1][1] == mas1[2][2] == mas1[3][3]== "0":
        ok = True
    
    elif mas1[1][3] == mas1[2][2] == mas1[3][1]== "+":
        ok = True
    elif mas1[1][3] == mas1[2][2] == mas1[3][1]== "0":
        ok = True

    else:
        ok= False    

winner = mas1[y][x]
print (f"Победил {winner}")

