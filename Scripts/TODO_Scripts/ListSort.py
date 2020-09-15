arr = [12, 820, 73, 23, 41, 0, -1, 0000.001, 1100.00, 101.001, 20, 560]
print("Unsorted Array: ",arr)

def selection_sort(array):
    for i in range(0,len(array)):
        minval=i                            # Assuming the minimum value is the first element 
        for j in range(i+1, len(array)):    # Updating the minimum value
            if array[minval] > array[j]: 
                minval = j

        array[i], array[minval] = array[minval], array[i] #swapping values to sort

    print ("After sorting: ", array)

selection_sort(arr)



