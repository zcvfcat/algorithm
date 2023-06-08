def permutations(array, tie):
    if tie == 0:
        return [[]]

    tied = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], tie - 1):
            tied += [value, *edges]
    
    return tied
