arr = [12, 82, 73, 23, 41, 0, -1, 0000.001, 1100.00, 101.001, 20, 560]

def Insertion_Sort(arr):                #Using Insertion Sort to sort the array
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

    print("The largest number: ",arr[-1]) # Prining the last element of the array.


Insertion_Sort(arr)

