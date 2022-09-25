# Напишите программу, которая принимает на вход координаты точки (X и Y)
# , причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).


x = int(input('Enter x '))
y = int(input('Enter y '))

if x != 0 and y !=0:   # ИНВЕРСИЯ!
    if x > 0 and y > 0:
        print ("1 quarter")
    if x < 0 and y > 0:
        print ("2 quarter")
    if x < 0 and y < 0:
        print ("3 quarter")
    if x > 0 and y < 0:
        print ("4 quarter")
else:
    print ("point on the axis")