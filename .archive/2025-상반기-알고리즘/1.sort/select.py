def select(array):
    for i in range(len(array)):
        cur = i
        for k in range(i + 1, len(array)):
            if array[cur] < array[k]:
                cur = k
        array[cur], array[i] = array[i], array[cur]

            