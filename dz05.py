# DZ 5 Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 
# ПРИЗНАЮСЬ решение скачано из сети - сижу пытаюсь понять как такие операции делать в принципе!!!

# ⋁ -  OR, |, ИЛИ, логическое сложение, дизъюнкция,
# /\ - AND, &, И, логическое умножение, конъюнкция
# ¬ - NOT, !,~, НЕ, отрицание, инверсия, 


# ввод данных
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
#################################################################
a = x * y * z 
b = x + y + z 

# инверсия для результатов
if a > 0:
    a = 0
elif a < 1:
    a = 1
if b > 0:
    b = 1
elif b < 1:
    b = 1

if a == b:
    print('Утверждение истинно')
elif a != b:
    print('Утверждение ложно')
###########################################################################
leftSide = not (x or y or z) # ¬(X ⋁ Y ⋁ Z)
rightSide = not x and not y and not z # ¬X ⋀ ¬Y ⋀ ¬Z
result = leftSide == rightSide

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
#######################################################################

# 3д и количество координат
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
########################################################################
trigger = True # буллева переменная

for x in [True,False]: # for x in range(2):
        for y in [True,False]:
            for z in [True,False]:
                if not (x or y or z) != (not x and not y and not z):
                    print ('NE VERNO')
                    trigger = False
                    break
if trigger: print ('VERNO')              

