def select(array):
    for i in range(len(array)):
        curr = i

        for k in range(i + 1, len(array)):
            if array[curr] > array[k]:
                curr = k

        array[curr], array[i] = array[i], array[curr]

    return array


print(select([44, 2, 3, 1, 4, 5, 243, 6]))
