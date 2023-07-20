def b1(sorted_array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    value = sorted_array[mid]

    if target > value:
        return b1(sorted_array, target, mid + 1, end)
    elif target < value:
        return b1(sorted_array, target, start, end - 1)
    else:
        return mid

def b2(array, target):
    array.sort()
    start, end = 0, len(array)
    
    while start <= end:
        mid = (start + end) // 2
        value = array[mid]

        if target > value:
            start = mid + 1
        elif target < value:
            end = mid - 1

        return mid

    return None
            