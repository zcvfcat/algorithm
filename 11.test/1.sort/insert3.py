def insert_asc(array):
    for start_idx in range(len(array)):
        search_idx = start_idx

        for current_idx in range(start_idx, len(array), 1):
            if array[search_idx] > array[current_idx]:
                search_idx = current_idx

        array[start_idx], array[search_idx] = array[search_idx], array[start_idx]
    
    return array

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(insert_asc(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(insert_asc(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(insert_asc(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(insert_asc(arr4) == expected_output4)