def bubble(array):
    for limit in range(len(array) - 1, -1, -1):
        for i in range(limit):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array