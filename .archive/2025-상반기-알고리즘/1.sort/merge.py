def merge(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    
    left, right = merge(array[:mid]), merge(array[mid:])
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged + left + right