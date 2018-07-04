#При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
li = list(map(lambda x: x%5, [1, 4, 5, 30, 99]))
print (li)

#При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
li = list(map(lambda x: str(x), [3, 4, 90, -2]))
print(li)

#При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
print(list(filter(lambda x: type(x) != str,  ['some', 1, 'v', 40, '3a', str])))

#При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
from functools import reduce
li = ['some', 'other', 'value']

for i in li:
    lo = list(i)
  #  print(reduce(lambda x: , lo))

my_list = [2, 5, 7, -6]

print([i * 2 for i in my_list if i > 0])