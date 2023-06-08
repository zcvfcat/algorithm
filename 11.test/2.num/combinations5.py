def combinations(array, tie):
    if tie == 0:
        return [[]]

    combined = []

    for node, value in enumerate(array):
        for edges in combinations(array[node:], tie - 1):
            combined += [value, *edges]

    return combined
