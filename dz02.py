# ДЗ 2 Напишите программу, которая будет принимать на вход дробь
#  и показывать первую цифру дробной части числа.

a = float (input("Задайте число:  "))
b = int ((a*10)%10)
print(b) 