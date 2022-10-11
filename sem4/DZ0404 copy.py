# DZ 4 -4 чужое РЕШЕНИЕ 


pathWrite = r"C:\Users\User\Desktop\Python\APython\DZ4\file4_4.txt"

# МЕТОД - ТРЕБУЕТ ВВОД СТЕПЕНИ, ВЫДАЕТ СЛУЧАЙНЫЙ МНОГОЧЛЕН ПО НЕЙ
from random import randint as rI
def createEquation():
    degree = int(input("Введите максимальную степень многочлена: "))
    equation = ''

    for d in range(degree, -1, -1):
        coef = rI(-20, 20)
        if d == degree:
            if coef > 0:
                equation += str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += '-' + str(abs(coef)) + 'x^' + str(d)
        else:
            if coef > 0:
                equation += ' + ' + str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += ' - ' + str(abs(coef)) + 'x^' + str(d)

    return equation + ' = 0'

a = createEquation()
print (a)

def readEquation():
    firstEquation = createEquation()
    eqation = {} # словарик

    firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2] # убрать = 0

    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])
        # словарик = [ключ] - [значение]

    return eqation

# цикл - Складывает два словаря
finalWord = {}

word1 = readEquation()
print (word1)
word2 = readEquation()
# выбрать макс длину из двух словарей для финального в обратном порядке
for i in range(max(len(word1), len(word2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0) # для работы OR  - присваивает знач 0

print(finalWord)




# try:
#     with open(pathWrite, "w") as data:
#         data.write('polynomial in grade {k}')
#         data.write("\n")
#         data.write(endF)
# except:
#     print("ОБЩИБКА РАБОТЫ С ФАЙЛОМ")
