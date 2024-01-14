def bubble(array):
    for l in range(len(array) - 1, -1, -1):
        for i in range(l):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array
    