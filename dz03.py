# ДЗ 3 Напишите программу, которая принимает на вход число и проверяет,
#  кратно ли оно 5 и 10 или 15, но не 30.

 
a = int (input("enter a number:  "))
if a%5 == 0:
    print ("multiple of 5")
if a%10 == 0:
    print ("multiple of 10")
if a%15 == 0:
    print ("multiple of 15")
if a%30 != 0 and a%5 == 0:
    print ("not multiple of 30")
if a%5 != 0:
    print ("the number does not match the condition")