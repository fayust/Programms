arr = [2, 1, 3, 13, 5, 17, 67, 1]

def change(first, sec):
    tmp = arr[first]
    arr[first] = arr[sec]
    arr[sec] = tmp

if __name__ == '__main__':
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                change(j-1, j)

    print('отсортированный массив: {}'.format(arr))