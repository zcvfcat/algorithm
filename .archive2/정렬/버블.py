def bubble(array):
    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    return array


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(bubble(arr))
