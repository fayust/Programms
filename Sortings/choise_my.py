
arr = [2, 43, 91, 5, 58, 34, 8, 56, 61]

def fun_min_el (first):
    ind_min = first
    for i in range(first, len(arr)):
        if arr[ind_min] > arr[i]:
            ind_min = i

    return ind_min

if __name__ == '__main__':
    for i in range(len(arr)):
        min_el = fun_min_el(i)
        if i == min_el:
            continue
        else:
            tmp = arr[i]
            arr[i] = arr[min_el]
            arr[min_el] = tmp

    print ("Отсортированный массив: {}".format(arr))


