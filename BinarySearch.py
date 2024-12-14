def binary_search(arr, item):
    left_index = 0
    right_index = len(arr)

    while left_index <= right_index:
        midpoint = (left_index + right_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif midpoint_value < item:
            left_index = midpoint + 1
        else:
            right_index = midpoint - 1
    return -1


arr = [1,2,3,4,5,6,7]
item = 3
print(binary_search(arr, item))
