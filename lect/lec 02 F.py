import lec # импортировать из - имя програмы
# если долгое название или оно уже используется - то пишем
# import lec as L

print(lec.f(1))# вывести (имя программы.название функции(аргумент))

# # здесь аргумент присваивается в функции - можно задавать 1
# def new_string (symbol, count = 3):
#     return symbol * count

def conc (*params):
    res: str = ""
    for i in params:
        res += i
    return res

print (conc('1','2','2','3')) # обязательно ''


# РЕКУРСИЯ - главное чтоб была точкак выхода
# Метод ФИБОНАЧИ!!! 
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range (1,10):
    list.append(fib(e))
print(list)


# словари
dict = {}
dict = \  
{
        'up':'1',
        'down':'2', 
        'left': '<',
        'right':'>'
}

print (dict)

for i in dict.keys():
    print(k)

#  Множества

а = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()# дубликат
u = a.union(b)# 0бьединение
i = a.intersection(b) # i = {8,2,5}
d1 = a.difference(b)# d1 = {1,3}
d2 = b.difference(a)# d1 = {13,21}
s = frozenset (a)# неизменяемое