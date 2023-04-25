def insert_sort(array: list, left, right):
    for node in range(left, right):
        idx = node

        while idx >= left and array[idx] > array[idx + 1]:
            array[idx + 1], array[idx] = array[idx], array[idx + 1]
            idx -= 1

arr1 = [3, 2, 1]
insert_sort(arr1, 0, 2)
print(arr1)
