# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
number = int(input('Введите натуральное число: '))
def SimpleMultiplys (num):
    i = 2
    arr = []
    while (i * i <= num):
        while (num % i == 0):
            arr.append(i)
            num=num/i
        i+=1
    if (num>1):
        arr.append(num)
    return arr
print(SimpleMultiplys(number))