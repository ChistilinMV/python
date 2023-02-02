# Урок 2. Циклы (for, while)
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input())
degree = 0
res = 1
while res < n:
    print(res, end = " ")
    res = res * 2
    degree += 1
