def insert2(array):
    for current in range(len(array)):
        select = current
        for check in range(select + 1, len(array)):
            if array[select] > array[check]:
                select = check
        
        array[select], array[current] = array[current], array[select]
    
    return array

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(insert2(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(insert2(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(insert2(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(insert2(arr4) == expected_output4)