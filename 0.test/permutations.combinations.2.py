def permutations(array, ties):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], ties - 1):
            merged.append((value, *edges))
    return merged


def combinations(array, ties):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], ties - 1):
            merged.append((value, *edges))
    return merged

# print(permutations([10, 3, 2],2))
print(combinations([10, 3, 2],2))