def quick(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []

    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)
    
    return quick(left) + equal + quick(right)

def merge(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left, right, merged = merge(arr[:mid]), merge(arr[mid:]), []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    return merged + left + right