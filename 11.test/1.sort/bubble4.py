def bubble(array):
    for i1 in range(0,len(array)-1):
        for i2 in range(i1, len(array)):
            if array[i1] > array[i2]:
                array[i1], array[i2] = array[i2], array[i1]
    return array