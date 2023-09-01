def select(arr):
    for idx in range(len(arr) - 1):
        curr = idx

        for search in range(idx, len(arr)):
            if arr[search] > arr[curr]:
                curr = search
        
        if curr != idx:
            arr[idx], arr[curr] = arr[curr], arr[idx]

    return arr
