def permutations(arr, ties):
    if ties < 2:
        return [[]]

    merged = []

    for node, value in enumerate(arr):
        for edges in permutations(arr[:node], arr[node + 1:], ties - 1):
            merged.append((value, *edges))
    
    return merged