def select(arr):
    for node in range(len(arr)):
        curr = node
        for edge in range(node + 1, len(arr)):
            if arr[curr] > arr[edge]:
                curr = edge

        arr[node], arr[curr] = arr[curr], arr[node]

    return arr
