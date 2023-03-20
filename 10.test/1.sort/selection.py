def selection(arr):
    for node in range(len(arr)):
        select = node

        for i in range(node, len(arr)):
            if arr[select] > arr[i]:
                select = i

        arr[select], arr[node] = arr[node], arr[select]

    return arr
