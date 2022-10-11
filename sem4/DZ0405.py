# DZ 4 - 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

pathRead1 = r"C:\Users\User\Desktop\Python\APython\DZ4\file4_5in1.txt"
pathRead2 = r"C:\Users\User\Desktop\Python\APython\DZ4\file4_5in2.txt"
pathWrite = r"C:\Users\User\Desktop\Python\APython\DZ4\file4_5out.txt" # r  чтобы в названия не растознались элементы кода


try:
    with open(pathRead1) as data1: 
        file1 = data1.read().split('')
    with open(pathRead2) as data2: 
        file2 = data2.read()
# TRY ..... если не прошло то пишет заместо ошибки
except:
    print("файл(ы) не найден(ы)")


for i in range(max(len(file1), len(file2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)

print(finalWord)


# try:
#     with open (pathWrite, "w") as data:
#         data.write(f'polynomial in grade {k}')
#         data.write("\n")
#         data.write(endF)
# except:
#     print ("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")



         
    





