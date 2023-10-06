def select(arr):
    for idx in range(len(arr)):
        curr = idx
        for j in range(idx, len(arr)):
            if arr[curr] > arr[j]:
                curr = j
        
        arr[curr], arr[idx] = arr[idx], arr[curr]

    return arr
