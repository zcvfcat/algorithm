def binary(arr, target):
    start, end = 0, len(arr) - 1
    arr.sort()

    while start <= end:
        mid = start + end
        value = arr[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return mid

    return None


print(binary([7, 1, 8, 2, 10, 3, 4, 9, 5, 6], 5))
