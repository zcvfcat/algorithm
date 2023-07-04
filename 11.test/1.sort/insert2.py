def insert(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] > array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array
