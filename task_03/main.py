#  Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
from random import randint

number = int(input('Введите размер последовательности чисел: '))
def OnlyUnical (num):
    if num <= 0:
        print('Negative value of the number of numbers!')
    arr = [randint(0,num*2) for i in range(0,num)]
    res = [i for i in arr if arr.count(i) == 1]
    return arr , res
print(OnlyUnical(number))