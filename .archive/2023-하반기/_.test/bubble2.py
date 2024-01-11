def bubble(arr):
    for limit in range(len(arr) -1, -1, -1):
        for i in range(limit):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr