# DZ 5_4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

pathRead = r"C:\Users\User\Desktop\Python\APython\DZ5\in.txt"
pathWrite1 = r"C:\Users\User\Desktop\Python\APython\DZ5\out.txt"
pathWrite2 = r"C:\Users\User\Desktop\Python\APython\DZ5\out copy.txt"

# МЕТОД Выполнение алгоритма сжатия данных кодирования длин серий (RLE)
#  для строки `str`
def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding

# Метод принимает сссылку на TXT и выдает строку с текстом
def strPathRead (pathRead):
    try:
        with open(pathRead) as data:  # оптимальный вариант
            file = data.read()   
    except:
        print("не найден")
    print (f' Полный текст:  {file}')
    return file

# МЕТОД Выполнение алгоритма восстановления данных  (RLE)
#  для строки `str`

def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # разделение закодированного сообщения на соответствующие счетчики
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # отображение символа несколько раз, указанным счетчиком
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message



fullFile = strPathRead(pathRead)
encodeFile = encode(fullFile)
print (f' Сжатый текст:  {encodeFile}')
decodeFile = decode(encodeFile)
print (f' Восстановленный текст:  {decodeFile}')


try:
    with open (pathWrite1, "w") as dataW:
        dataW.write(encodeFile)
except:
    print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")

try:
    with open (pathWrite2, "w") as datav:
        datav.write(decodeFile)
except:
    print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")










# i= 0
# count = 1

# for i in range (len(listIn)-1):


#     if  listIn[i] != listIn[i+1]:
#         listOut.append (f'{count}{listIn[i]}') 
#         count = 1
#     else:
#         count+=1
#         i+=1
# print(listOut)



