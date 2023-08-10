def combinations(array, tie):
    if tie == 0:
        return [[]]

    tied = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], tie - 1):
            tied += [(value, *edges)]

    return tied


array = [1, 2, 3, 4, 5]
tie = 3

print(combinations(array, tie))
