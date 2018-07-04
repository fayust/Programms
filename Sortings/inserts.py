'''Вставками

Алгоритм примерно такой:

    из массива последовательно берется каждый элемент
    вставляется в его отсортированную часть(например в начале массива)
'''

def isort(array):
    for i in range(len(array)):
        v = array[i]
        j = i
        while (array[j-1] > v) and (j > 0):
            array[j] = array[j-1]
            j = j - 1
        array[j] = v
        print (array)
    return array