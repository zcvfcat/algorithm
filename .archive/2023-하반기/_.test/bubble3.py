def bubble(array):
    for limit in range(len(array) - 1, -1, -1):
        for idx in range(limit):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
    
    return array