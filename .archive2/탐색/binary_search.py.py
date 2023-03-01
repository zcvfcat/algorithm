def binary_search(array, value):
    array.sort()
    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if value > array[mid]:
            left = mid + 1
        elif value < array[mid]:
            right = mid - 1
        else:
            return mid


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(array, 3))
