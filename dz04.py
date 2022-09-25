# DZ 4 Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет, является ли этот день выходным.

a = int (input("enter a day number:  "))
if a < 6:
    print ("weekday")
elif a > 5 and a < 8:
    print ("weekend")
else:
    print ("incorrect number") 