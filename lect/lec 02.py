# другой способ
with open ('file.txt', 'w') as data:
    data.write('\n Line 2\n')
    data.write('\n Line 3\n')
#  Close  не надо - автоматически работает

colors = ['red', 'green','blue']#набор данных
data = open ('file.txt', 'a')# текстовая переменная дата, связ с текст файлом, мод (a,r,w.....)
data.writelines(colors)#  дописать данные , разделителей не будет!!!
data.write('\n Line 2\n')# \n - переход новая строка
data.close()# закрыть (иначе файл занят)

# чтение данных

path = 'file.txt' # текст переменная
data = open(path,'r')# открыть для чтения
for line in data:# пробежать по свем строкам файла и прочитать
    print(line)# вывести
data.close()# закрыть
