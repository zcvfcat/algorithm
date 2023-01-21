def insert(array) -> list:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(insert(arr))
