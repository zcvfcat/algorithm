def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

def binary_search_recursive(array, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, right)
    else:
        return binary_search_recursive(array, target, left, mid - 1)

print(binary_search_recursive(sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5, 0, 9))