def combinations(arr, ties):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(arr):
        for edges in combinations(arr[node + 1:], ties - 1):
            merged.append((value, *edges))
    return merged
