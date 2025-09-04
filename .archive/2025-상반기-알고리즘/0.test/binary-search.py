def binary_search(arr, target):
    left, right = 0, len(arr)
    arr.sort()

    while left <= right:
        mid = (left + right) // 2
        value = arr[mid]

        if value < target:
            left = mid + 1
        elif value > target:
            right = mid - 1
        else:
            return mid
    return None

def binary_search_recur(arr, target, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    value = arr[mid]

    if value < target:
        binary_search_recur(arr, target, mid + 1, right)
    elif value > target:
        binary_search_recur(arr, target, left, mid - 1)
    else:
        return mid
    
