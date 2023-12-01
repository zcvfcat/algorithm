def binary_recur(arr, target, start, end):
    if start >= end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] < target:
        return binary_recur(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_recur(arr, target, start, mid - 1)

    return mid

def binary(arr, target):
    start = 0
    end = len(arr)
    arr.sort()

    while start < end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] < target:
            end = mid - 1
        else:
            return mid
