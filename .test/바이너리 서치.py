array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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
    else:
        return False


print(binary_search(array, 3))


def binary_search_recur(array, value, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if value > array[mid]:
        return binary_search_recur(array, value, mid + 1, right)
    elif value < array[mid]:
        return binary_search_recur(array, value, left, mid - 1)
    else:
        return mid


print(binary_search_recur(sorted(array), 3, 0, len(array) - 1))
