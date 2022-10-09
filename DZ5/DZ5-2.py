# DZ 2-2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


print ('На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можнозабрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
print ('Выберите режим игры:')
print ('1 - Игра с другом')
print ('2 - Игра с ТУПЫМ БОТОМ')
print ('3 - Игра с МЕГАБОТОМ')

#МЕТОД _ ИГРА В КОНФЕТЫ ДВА ИГРОКА
def multiplayer():
    # ввод игроков:
    player1 = input ('введите имя Игрока 1:  ')
    player2 = input ('введите имя Игрока 2:  ')

    firstLot = player1
    secondLot = player2

    #определение кто первый ходит
    import random
    lot = random.randint (1, 2)
   
    if lot == 2:
        firstLot = player2
        secondLot = player1
    print (f'первым ходит - {firstLot}')



    # игра в конфетки
    count = 150

    winner = firstLot

    while count > 0:
        count = count - int(input(f'Ходит {firstLot} -  '))
        print(f'Остаток:  {count}')
        winner = firstLot
        if count > 0:
            count = count - int(input(f'Ходит {secondLot} -  '))
            print(f'Остаток:  {count}')
            winner = secondLot
        else:
            winner = firstLot
    print (f' Победитель: {winner}!')

#МЕТОД _ ИГРАть с ботом выдающим случайные числа от 1 до 28
def stupidBot():
    # ввод игроков:
    player1 = input ('введите свое имя:  ')
    player2 = ('ТУПОЙ БОТ')

    
    count = 150
    winner = player1

    #определение кто первый ходит
    import random
    lot = random.randint (1, 2)
    
   
    
    if lot == 1:
        print (f'первым ходит - {player1}')
        while count > 0:
            count = count - int(input(f'Ходит {player1} -  '))
            print(f'Остаток:  {count}')
            winner = player1
            if count > 0:
                steep = random.randint (1, 28)
                print (f'Ходит {player2} - {steep}')
                count = count - steep
                print(f'Остаток:  {count}')
                winner = player2
            else:
                winner = player1
    if lot == 2:
        print (f'первым ходит - {player2}')
        while count > 0:
            steep = random.randint (1, 28)
            print (f'Ходит {player2} - {steep}')
            count = count - steep
            print(f'Остаток:  {count}')
            winner = player2
            if count > 0:
                count = count - int(input(f'Ходит {player1} -  '))
                print(f'Остаток:  {count}')
                winner = player1
            else:
                winner = player2

    print (f' Победитель: {winner}!')

#МЕТОД _ ИГРАть с ботом выдающим случайные числа от 1 до 28
def megaBot():
    # ввод игроков:
    player1 = input ('введите свое имя:  ')
    player2 = ('МЕГАБОТ')

    
    count = 150
    winner = player1

    #определение кто первый ходит
    import random
    lot = random.randint (1, 2)
    
   
    
    if lot == 1:
        print (f'первым ходит - {player1}')
        while count > 0:
            count = count - int(input(f'Ходит {player1} -  '))
            print(f'Остаток:  {count}')
            winner = player1
            if count > 0:
                steep = random.randint (1, 28)
                print (f'Ходит {player2} - {steep}')
                count = count - steep
                print(f'Остаток:  {count}')
                winner = player2
            else:
                winner = player1
    if lot == 2:
        print (f'первым ходит - {player2}')
        while count > 0:
            steep = random.randint (1, 28)
            print (f'Ходит {player2} - {steep}')
            count = count - steep
            print(f'Остаток:  {count}')
            winner = player2
            if count > 0:
                count = count - int(input(f'Ходит {player1} -  '))
                print(f'Остаток:  {count}')
                winner = player1
            else:
                winner = player2

    print (f' Победитель: {winner}!')
# выбор режима игры
gameMod = input('Режим игры:   ')
if gameMod == '1':
    multiplayer()
if gameMod == '2':
    stupidBot()
if gameMod == '3':
    megaBot()
else: 
    print ('еще разок......')