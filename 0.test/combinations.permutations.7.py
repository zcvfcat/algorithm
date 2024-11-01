def combinations(array, ties=1):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], ties - 1):
            merged.append((value, *edges))

    return merged


def permutation(array, ties=1):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in permutation(array[:node] + array[node + 1:], ties - 1):
            merged.append((value, *edges))

    return merged
