def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

arr = [2,1,3,4,12,5,14,6,7,19,20,7,9,20]
print(bubblesort(arr))