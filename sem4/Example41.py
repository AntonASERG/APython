# Задача 4-1. Считать из файла список чисел, написать программу котарая найдет мин и мах  и запишет в отд Файл.

data = open('file.txt','r')# открыть для чтения
file = data.read().split(" ")# прочитать (переписать на черновик) SPLIT ("Pa3DeLITEL ")
data.close()# закрыть 
print (file)
# File -  список строк

# цикл - перевести  массив строк в массив ИНТ!
for i in range (len(file)):# пробежать по длине ФАЙЛА
    if file[i].isdigit: #  проверка(доп) не ввели ли где буквы
        file[i] = int (file[i]) # перевод элементов в ИНТ
print (file)
print (min(file))
print (max(file))
# дописать данные в новый файл
data = open(r'file2.txt','w')# создать и открыть новый файл
data.write(f'{min(file)}, {max(file)}\n')#  дописать данные, \n - переход новая строка
data.close()# закрыть  



