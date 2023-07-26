def quick(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr)//2]
    left, equal, right = [], [], []

    for v in arr:
        if v == pivot:
            equal += [v]
        elif v < pivot:
            left += [v]
        else:
            right += [v]
    
    return quick(left) + equal + quick(right)