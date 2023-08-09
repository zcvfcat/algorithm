def bubble(array):
    for end in range(len(array) -1, -1, -1):
        for curr in range(end):
            next = curr + 1

            if array[curr] > array[next]:
                array[curr], array[next] = array[next], array[curr]

    return array