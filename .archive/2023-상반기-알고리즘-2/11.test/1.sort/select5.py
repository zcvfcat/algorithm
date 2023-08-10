def select(arr):
    for i in range(len(arr)):
        s = i
        for j in range(i,len(arr)):
            if arr[s] > arr[j]:
                s = j
        
        arr[s], arr[i] = arr[i], arr[s]
    
    return arr
