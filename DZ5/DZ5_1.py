# DZ 5 - 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


strText = input ('Введите текст через пробел:  ')
print (strText)

# метод принимает строку, требует ввода фильтра 
# и возвращает строку с элементами не содержащими фильтр
def elemFilter (str):

    listText = str.split()
    strElem = input ('Введите элемент для поиска и удаления:  ')
    print (strElem)

    listCut = []
    strCut = ''

    for i in range(len(listText)):
        if listText[i].find(strElem) == -1:
            listCut.append(listText[i])
    strCut = ' '.join(listCut) # перевести массив в строку с разд. пробел
    return strCut

print(elemFilter(strText))


