def bubble2(array):
    for limit in range(len(array) -1, -1, -1):
        for current_idx in range(limit):
            current = array[current_idx]
            next = array[current_idx + 1]
            
            if current > next:
                array[current_idx], array[current_idx + 1] = array[current_idx + 1], array[current_idx]
    
    return array


# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(bubble2(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(bubble2(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(bubble2(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(bubble2(arr4) == expected_output4)
