def quick2(array):
    if len(array) < 2:
        return array

    pivot = array[len(array)//2]
    left, equal, right = [], [], []

    for value in array:
        if value < pivot:
            left.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            right.append(value)

    return quick2(left) + equal + quick2(right)


# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(quick2(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(quick2(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(quick2(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(quick2(arr4) == expected_output4)
