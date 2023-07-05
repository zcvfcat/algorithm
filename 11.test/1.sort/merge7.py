def merge(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left, right, merged = merge(array[:mid]), merge(array[mid:]), []

    while left and right:
        merged += [left.pop(0)] if left[0] < right[0] else [right.pop(0)]
    
    return merged + left + right

