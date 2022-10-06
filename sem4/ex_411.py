# работа с текстами

pathRead = r"file.txt"
pathWrite = r"file2.txt" # r  чтобы в названия не растознались элементы кода

# команда - ПОПРОБУЙ СДЕЛАЙ ЭТО:
try:
    with open(pathRead) as data:  # оптимальный вариант
        file = data.read().split(" ")
# TRY ..... если не прошло то пишет заместо ошибки
except:
    print("не найден")

print (file)
listInt = []

# for i in range(len(file)): 
#     if file[i].isdigit():
#         file[i] = int (file[i]) # чтобы перезаписать  работаем с индексами
# ненужные элементы остались

# print (file)


for elem in file: 
     if elem.isdigit():
            listInt.append(int(elem))
print (listInt)
print (max(listInt))
print (min(listInt))

try:
    with open (pathWrite, "w") as data:
        data.write(str(min(listInt)))
        data.write("\n")
        data.write(str(max(listInt)))
except:
    print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")