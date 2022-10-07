# # def sum (x,y):
# #     return x+y
# # =
# # sum = lambda x, y: x+y


# # f = sum        присвоили переменной функцию

# def mylt (x,y):
#     return x*y

# def calc (op, a, b):
#     print (op(a,b))
#     # return (op,(a,b))

# # calc(sum, 4, 5)
# calc(lambda x, y: x+y, 4, 5)

# # ==========================================================================
# # List Comprehension
# def f(x):
#     return x**3

# list = [ i for i in range (1,101) if i%2 == 0]
# list = [ (i,i) for i in range (1,101) if i%2 == 0]#кортеж пары
# list = [ f(i) for i in range (1,101) if i%2 == 0]# массив функций от х
# list = [ (i,f(i)) for i in range (1,101) if i%2 == 0]# массив пар х, f(x)

# # ==========================================================================

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

pathRead = r"C:\Users\User\Desktop\Python\text.txt"

try:
    with open(pathRead, "r") as f:  
        data = f.read().split() # type - list
except:
    print("не найден")

def select (f,col):
    return [f(x) for x in col]

def where (f,col):
    return [x for x in col if f(x)]

res = select(int, data) # f- int преобразовать
res = where(lambda x: not x%2, res) # отсеять четные
res = select(lambda x: (x,x**2), res) # составить список пар
print (res)
# 1 2 3 5 8 15 23 38
# numbers = []

# while data != '': # != ничему
#     space_pos = data.index(' ') # найти 1 позицию символа ' ' (пробела)
#     numbers.append(int(data[: space_pos]))# ,берем все что до пробела и превр в инт
#     data = data[space_pos+1:] # что то типа счетчика чтоб исл иск пробелы

# print (numbers)
# # [1, 2, 3, 5, 8, 15, 23, 38]

# out = []

# for e in numbers:
#     if not e%2:
#         out.append((e, e**2))
# print (out)



