def select(array) -> list:
    for i in range(len(array)):
        index = i

        for j in range(i + 1, len(array)):
            if array[index] > array[j]:
                index = j

        array[i], array[index] = array[index], array[i]
    return array


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(select(arr))
