def selection(arr):
    for i in range(len(arr)):
        pick = i

        for k in range(i,len(arr)):
            if arr[pick] > arr[k]:
                pick = k
        
        arr[pick], arr[i] = arr[i], arr[pick]
    
    return arr
        