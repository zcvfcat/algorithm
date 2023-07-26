def merge(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = merge(arr[:mid]), merge(arr[mid:])
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged += [left[0]]
        else:
            merged += [right[0]]
    
    return merged + left + right
    