# -*- coding: utf-8 -*-





def factorial(n):
    if n == 0:
        return 1
    else:
        x = n * factorial(n - 1)
        print(x)
        return x

print(factorial(6))


'''

Число фибоначчи равно сумме двух предыдущих. Начинается с 1, второе тоже 1.
def fib(n)
if n>2 return fib(n-1)+fib(n-2)
else return 1'''