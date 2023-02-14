# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def ab(i, k):
    if k == 1:
        return i
    else:
        return i * ab(i, k - 1)

a = int(input('Enter A = '))
b = int(input('Enter B = '))
print(ab(a,b))
