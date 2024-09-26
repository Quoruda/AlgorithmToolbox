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
