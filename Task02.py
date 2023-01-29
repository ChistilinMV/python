# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите 3-х значное число >')
if len(number) > 3:
    number = number[0:3]
    print('В числе больше 3-х знаков. Будут просуммированы первые три >', number)
number = int(number)
summ = 0
while number > 0:
    tmp = number % 10
    summ += tmp
    number //= 10
print('Сумма цифр =', summ)
