def quick(arr):
    if len(arr) < 2:
        return arr
    
    k = arr[len(arr) // 2]

    left, equal, right = [],[],[]

    for v in arr:
        if v < k:
            left.append(v)
        elif v > k:
            right.append(v)
        else:
            equal.append(v)
    
    return quick(left) + equal + quick(right)
    