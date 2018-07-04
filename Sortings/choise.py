'''Сортировка выбором — здесь, чтобы отсортировать массив, находим элемент с минимальным значением, 
затем сравниваем его со значением первой неотсортированной позиции. Если этот элемент меньше, то он становится 
новым минимумом и их позиции меняются.'''

def ssort(array):
    for i in range(len(array)):
        indxMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return (array)