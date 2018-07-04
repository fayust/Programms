'''Функция принимает на вход одно из 3-х исключений ValueError, TypeError, RuntimeError случайным образом.
 В месте вызова функции обрабатывать все 3 исключения
 '''


import random


li = [ValueError, TypeError, RuntimeError]
i = random.randint(0,3)

def func1(i):
    raise li[i]


try:
    func1(i)
except ValueError:
    print('Ошибка значения')
except TypeError:
    print("Ошибка типа")
except RuntimeError as e:
    print("Ошибка рантайм", e)



'''Функция принимает на вход список. Если все объекты инт - сортирует его, иначе выбрасывает  ValueError'''



li1 = [1, 2, 9, 3, 4, None]


def func2(li1):
    flag = True

    for i in li1:
        if not isinstance(i, int):
            flag = False
    if flag == True:
        li1.sort()
    else:
        raise ValueError

    return li1

try:
    print(func2(li1))
except ValueError:
    print('Ошибка значения int')



#функция принимает словарь, преобразует все ключи к строкам и возвращает новый словарь

di = {1:'cat', 'rt':'dog', '5': 'meat' }

def func3(dic):
    di_new = dic
    for key in di_new:

        key =  str(key)


    return di_new

di1 = func3(di)
print(di1)
print(di1.keys())
print(di1[1])






