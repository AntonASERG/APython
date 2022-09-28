# # Задача 1-3 Напишите программу, в которой пользователь будет задавать
#  две строки, а программа - определять количество вхождений одной 
# строки в другой.
# ввод строк - инпут по умолчанию - СТРОКА!!!! 
s1 =  input('введите стр1 ')
s2 =  input('введите стр2 ')

# буфферные строка и подстрока - определить кто есть кто
string = ''
substring = ''

if len(s1) > len(s2):
    string = s1
    substring = s2
else:
    string = s2
    substring = s1
# метод - проверить количество подстрок в строке
print (string.count(substring))

# механика метода COUNT
count = 0
counter = 0

for i in range (len(string)- len(substring)):
    if string [i] == substring[0]:
        counterIn = 0
        for k in range(len(substring)):
            if substring [0+k] == string [i+k]:
                counterIn += 1
        if counterIn == len (substring):
            counter += 1
print(f'Counter = {counter}')


#  поиск подстроки в строке
# print (s1.find(s2))
# print (s2.find(s1))