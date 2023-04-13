def merge2(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    left = merge2(array[:mid])
    right = merge2(array[mid:])

    combined = []

    while left and right:
        if left[0] <= right[0]:
            combined.append(left.pop(0))
        elif right[0] < left[0]:
            combined.append(right.pop(0))
    
    combined.extend(left)
    combined.extend(right)
    
    return combined


# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(merge2(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(merge2(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(merge2(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(merge2(arr4) == expected_output4)