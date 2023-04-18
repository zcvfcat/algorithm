def shell(arr):
    n = len(arr)

    gap = n // 2

    while gap > 0:

        for current_idx in range(gap, n):
            select = arr[current_idx]

            select_idx = current_idx

            while select_idx >= gap and arr[select_idx - gap] > select:
                arr[select_idx] = arr[select_idx - gap]
                select_idx -= gap

            arr[select_idx] = select
        
        gap //= 2
    
    return arr

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(shell(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(shell(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(shell(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(shell(arr4) == expected_output4)
