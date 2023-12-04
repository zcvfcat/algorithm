def merge(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left , right , merged = merge(arr[:mid]), merge(arr[mid:]), []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        elif right[0] > left[0]:
            merged.append(right.pop(0))
    
    return merged + left + right
    
            
