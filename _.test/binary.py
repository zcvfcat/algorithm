def binary_search(array, target):
    start, end = 0, len(array)
    array.sort()

    while start < end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    
    return None

def recur_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] < target:
        recur_search(array,target, mid + 1, end)
    elif array[mid] > target:
        recur_search(array, target, start, mid - 1)
    else:
        return mid
