def combinations(array: list[int], ties: int):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edge in combinations(array[node + 1:], ties - 1):
            merged.append((value, *edge))
    return merged


def permutations(array: list[int], ties: int):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edge in permutations(array[:node] + array[node + 1:], ties - 1):
            merged.append((value, *edge))
    return merged
