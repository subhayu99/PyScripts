arr = [12, 820, 73, 23, 41, 0, -1, 0000.001, 1100.00, 101.001, 20, 560]
print("Before sorting: ", arr)

def selection_sort(arr):
    for i in range(len(arr)):
        minval=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minval]:
                minval=j
        arr[i], arr[minval] = arr[minval], arr[i]

    print("After sorting: ",arr)

selection_sort(arr)

