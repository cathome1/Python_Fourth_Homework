#  Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
from random import randint

number = int(input('Введите размер последовательности чисел: '))
arr = [randint(0,number*2) for i in range(0,number)]
res = [i for i in arr if arr.count(i) == 1]
print(arr)
print(res)