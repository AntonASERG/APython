# Задача 2-3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
count = 0
findWord = "qwe"

for i in range(len(list)):
    if list[i] == findWord:
        count +=1
        if count == 2:
            print(i)
            break
else:
    print("Error")
