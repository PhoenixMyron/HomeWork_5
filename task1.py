# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def result(a, b):
    if b == 1:
        return a
    else:
        return a * result(a, b - 1)

a = int(input("Write first number: "))
b = int(input("Write second number: "))
print(result(a, b))
