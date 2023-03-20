def bubble(array):
    for max_scope in range(len(array) - 1, -1, -1):
        for node in range(max_scope):
            next_node = node + 1

            val = array[node]
            next = array[next_node]

            if val > next:
                array[node], array[next] = array[next], array[node]
    return array
