def combinations(arr, ties):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(arr):
        for edges in combinations(arr[node + 1:], ties - 1):
            merged.append((*edges, value))

    return merged


def permutations(arr, ties):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(arr):
        for edges in permutations(arr[:node] + arr[node + 1:], ties - 1):
            merged.append((*edges, value))

    return merged
