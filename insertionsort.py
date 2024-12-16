def inserion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j] < arr[j-1] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr

arr = [2,6,5,1,3,4]
print(inserion_sort(arr))