# Задача 2-2 Задайте список. Напишите программу, которая 
# определит, присутствует ли в заданном списке строк некое число.

my_list = ["абвг123", "привет", "как дела", "10101"]
trigger = False

for i in range (len(my_list)):
    if my_list[i].find("3") >= 0: 
        trigger = True
        break
if trigger: # trigger = True
    print (" з есть")
else:
    print("3 нету")
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
list = ['s54dg5sg', 'sdf45sfs564fsdfs', 'sf45sda56sa', 'a0sa546s879dfg']
number = int(input('введите искомое число: '))
count = False
for i in list:
    for j in i:
        if j.isdigit() == True:
            if int(j) == number:
                count = True
                break
if count == True:
    print ('Есть')
else:
    print('Нет')

# ===================================================

string = ['asdfs4fhg', 'fds4wr', 'ewe45fgvsdg']
num = input("Введите число: ")


for element in string:
    if num in element:
        print("Присутствует")
        break
else:
    print("Отстутсвует")


