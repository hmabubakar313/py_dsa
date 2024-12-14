def rotate_list(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        midpoint = (left + right) // 2
        if nums[midpoint] < nums[right]:
            right = midpoint  # Move `right` to `midpoint` because the minimum is on the left
        else:
            left = midpoint + 1  # Move `left` to `midpoint + 1` because the minimum is on the right
    return nums[left]

# Test with the input list
input_list = [5, 6, 9, 0, 2, 3, 4]
print(rotate_list(input_list))  # Output should be 3
