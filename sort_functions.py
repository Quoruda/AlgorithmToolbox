def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index] 
        arr[min_index] = temp
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j] 
                arr[j] = temp
                
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def counting_sort(arr:[int]):
    vMax = arr[0]
    vMin = arr[0]
    for e in arr:
        if e > vMax:
            vMax = e
        elif e < vMin:
            vMin = e
    d = vMax-vMin
    countingArr = [0 for _ in range(d+1)]
    for e in arr:
        countingArr[e-vMin] += 1
    iArr = 0
    for i, count in enumerate(countingArr):
        for j in range(count):
            arr[iArr] = i+vMin
            iArr += 1


def fusion(arr:[int], s, m, e):
    i = s
    j = m+1
    k = s
    temp = [0 for _ in range(e+1)]
    while i <= m and j <= e:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= e:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(s, e+1):
        arr[i] = temp[i]
    return arr

def merge_sort(arr:[int], s, e):
    global n
    n += 1
    if s >= e:
        return arr
    m = (s+e)//2
    merge_sort(arr, s, m)
    merge_sort(arr, m+1, e)
    return fusion(arr, s, m, e)

