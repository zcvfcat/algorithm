def quick(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    less, equal, more = [], [], []

    for value in array:
        if value < pivot:
            less += [value]
        elif value == pivot:
            equal += [value]
        else:
            more += [value]

    return quick(less) + equal + quick(more)

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(quick(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(quick(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(quick(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(quick(arr4) == expected_output4)