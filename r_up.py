def find_runner_up(arr):
     
    sorted_array = sorted(arr, reverse=True)
    
    for i in range(len(sorted_array)):
        if sorted_array[i] != sorted_array[i+1]:
            return sorted_array[i+1]
            break

if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]
    result = find_runner_up(arr)
    print(result)
