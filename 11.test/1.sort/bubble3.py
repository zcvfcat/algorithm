def bubble_asc(array):
    for search_length in range(len(array) - 1, - 1, - 1):
        for idx in range(search_length):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
    
    return array

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(bubble_asc(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(bubble_asc(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(bubble_asc(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(bubble_asc(arr4) == expected_output4)