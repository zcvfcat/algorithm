from collections import deque

def insert(arr, start, end):
    for i in range(start, end):
        while i > start and arr[i] < arr[i - 1]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr

def merge(arr, start, mid, end):
    left, right, merged = deque(arr[start:mid]), deque(arr[mid:end]), []
    
    while left and right:
        merged += [left.popleft()] if left[0] < right[0] else [right.popleft()]
    
    return merged + left + right

def tim(arr, unit = 32):
    size = len(arr)
    for i in range(0, size, unit):
        arr = insert(arr, i, min(i + unit, size))
    
    while unit < size:
        for i in range(0, size, unit * 2):
            mid = i + unit - 1
            end = min(i + unit * 2 - 1, size)
            merged = merge(arr, i, mid, end)

            arr[i: i + len(merged)] = merged
        
        unit *= 2
    
    return arr