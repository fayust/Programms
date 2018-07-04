# Задача вернуть 1-е число последовательности фибоначи, которое делиться на 17. Фибо начинается с 1,1 след член равен сумме 2-х пред.

'''Это решение без callback
def fibonacci():
    values = []
    while (True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]
        if values[-1] % 17 == 0:
            return (values[-1])

        if values[-1] > 10000:
            return
if __name__ == '__main__':
    res = fibonacci()
    if (res != None):
        print(res)
'''


def fibonacci(cb):
    values = []
    while (True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        r = cb(values[-1])
        if (r[0]):
            return (r[1])

def check_17(v):
    if v % 17 == 0:
        return (True, v)

    if v > 10000:
        return (True, None)

    return (False,)

if __name__ == '__main__':
    res = fibonacci(check_17)
    if (res != None):
        print(res)