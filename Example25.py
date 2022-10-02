# Задача 2-5. Допы
# .find_parents() и .find_parent() ищут совпадения в родительских тегах.
# .find_next_siblings() ищет все совпавшие последующие одноуровневые элементы.
# .find_next_sibling() ищет первый совпавший последующий одноуровневый элемент.
# .find_previous_siblings ищет все совпавшие предшествующие одноуровневые элементы.
# .find_previous_sibling ищет первый совпавший предыдущий одноуровневый элемент.
# .find_all_next() ищет все совпавшие последующие элементы.
# .find_next() ищет следующий совпавший элемент.
# .find_all_previous ищет все совпавшие предшествующие элементы.
# .find_previous() ищет предыдущий совпавший элемент.

import random

number = int(input("введите число: "))

listInt = []

for i in range (number):
    listInt.append(random.randint(-number,number))

print (listInt)

position = ''
with open('text.txt', 'r') as data:
    position.append(data.read()).split('\n')

print(listInt[int(position[0])]*listInt[int(position[1])])