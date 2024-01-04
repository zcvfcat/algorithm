def binary_recur(array:list[int], target:int, start:int, end:int):
    if start > end:
        return None

    mid = start + ((end - start) // 2)
    value = array[mid]

    if value < target:
        return binary_recur(array, target, mid + 1, end)
    elif value > target:
        return binary_recur(array, target, start, mid - 1)
    
    return mid

def binary(array, target):
    start, end= 0, len(array)
    
    while start <= end:
        mid = start + ((end - start) // 2)
        value = array[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        
        return mid

    return None