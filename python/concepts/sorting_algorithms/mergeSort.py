def mergeSort(arr):
    if len(arr) < 2:
        return arr

    middleIndex = int(len(arr)/2)
    leftArr = arr[0:middleIndex]
    rightArr = arr[middleIndex:len(arr)]

    return mergeSort(leftArr) + mergeSort(rightArr)


l = [6,1,23,3,0]
r = mergeSort(l)

print(r)
