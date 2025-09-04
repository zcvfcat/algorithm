def permutations(array, tie):
    if tie < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edge in permutations(array[node + 1:] + array[:node], tie):
            merged.append((value, *edge))
    return merged

def combinations(array, tie):
    if tie < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edge in combinations(array[node + 1:], tie):
            merged.append((value, *edge))
    
    return merged