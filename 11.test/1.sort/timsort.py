# left ~ right 구간 삽입 정렬
def insert_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def merge(arr, start, midpoint, end):
    first_half = arr[start:midpoint + 1]
    last_half = arr[midpoint + 1: end + 1]
    merged_arr, i, j = [], 0, 0

    while i < len(first_half) and j < len(last_half):
        if first_half[i] < last_half[j]:
            merged_arr.append(first_half[i])
            i += 1
        else:
            merged_arr.append(last_half[j])
            j += 1

    merged_arr += first_half[i:]
    merged_arr += last_half[i:]

    return merged_arr


def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insert_sort(arr, i, min(i + min_run - 1, n - 1))

    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            merged_arr = merge(arr, start, midpoint, end)
            arr[start: start + len(merged_arr)] = merged_arr
        size *= 2

    return arr



# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(tim_sort(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(tim_sort(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(tim_sort(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(tim_sort(arr4) == expected_output4)
