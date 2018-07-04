arr = [4, 5, 77, 2, 33]

def change(first, sec):
    tmp = arr[first]
    arr[first] = arr[sec]
    arr[sec] = tmp

if __name__ == '__main__': # код исполниться только если файл запущен напрямую, а не импортирован из другого модуля - файла

    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j-1] > arr[j]:
                change(j-1, j)

    print("Отсортированный массив:{}".format(arr))
