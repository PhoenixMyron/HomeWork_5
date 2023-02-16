# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def suma_find(a, b):
    if b == 0 :
        return a
    else:
        return suma_find(a + 1 , b - 1)

a = int(input("Write first number: "))
b = int(input("Write second number: "))
print(suma_find(a, b))
