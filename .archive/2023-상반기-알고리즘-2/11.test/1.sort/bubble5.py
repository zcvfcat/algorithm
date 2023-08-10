def bubble(arr):
    for k in range(len(arr) -1, -1, -1):
        for i in range(k):
            if arr[i] > arr[i + 1]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr