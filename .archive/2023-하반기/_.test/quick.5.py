def quick(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, right, equal = [], [], []

    for v in arr:
        if v < pivot:
            left.append(v)
        elif v> pivot:
            right.append(v)
        else:
            equal.append(v)
    
    return quick(left) + equal + quick(right)