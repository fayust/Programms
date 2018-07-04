#генератор возвращает каждый раз новое случайное значение
import random
def gen():
    while True:
        yield random.randint(2,45)

x = gen()
#while True:
 #   print(next(x))


#генератор который работал бы как range
x = range(1,8,2)

def gen1(x1,y1,z1):

    while x1 < y1:
        yield x1
        x1 += z1

x1 = 2
y1 = 8
z1 = 1
y = gen1(x1,y1,z1)

try:
    while x1 < y1:
        print(next(y))
        x1+=z1
except StopIteration:
    print('значения закончились')



#генератор работающий как zip
s = [1, 2]
v = ['a', 'b']
def myzip(first, second):
    for i in range(len(first)):
        yield first[i], second[i]

z = myzip(s, v)
print(next(z))
print (next(z))



#генератор работающий как reduce
s = [1, 2]
v = ['a', 'b']
def myreduce(func, array, initial=0):
    for i array:
        result(func(item))





