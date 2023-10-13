def insert(arr, start, end):
    for i in range(start, end):
        while start < i and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i-=1

    return arr
            

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

    merged.extend(left)
    merged.extend(right)

    return merged

def tim(arr):
    unit = 32    