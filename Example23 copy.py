# Задача 2-4. Реализуйте алгоритм задания случайных чисел без использования
#  встроенного генератора псевдослучайных чисел.

def randomize(min, max):
    num = int(time.time_ns()/2000000)
    print(num)
    # while num > max:
    #     num /= max
    return int(num%max)

print(randomize(1,15))
