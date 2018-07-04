#Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!

def cancel_decorator(func):
    def inner(text):
        print("{} is canceled!".format(func.__name__))
    return inner

@cancel_decorator
def my_func(text):
    print ('Hello,{}'.format(text))

my_func('hhhhhhhhhh')

#Реализовать декоратор, который измеряет скорость выполнения функций.
import time

def time_decorator(func):
    def inner(val):
        start = time.time()
        ret = func(val)
        res_time = time.time() - start
        print ('Время выполнения функции {} {}'.format(func.__name__, res_time*1000))
        return ret
    return inner


@time_decorator
def my_func1(val):
    yu = 0
    for i in range(val):
        yu += i**2
    return yu

print('yu=',my_func1(5607))


