def combinations(array: list[int], ties=1):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], ties - 1):
            merged.append((value, *edges))

    return merged


array = [1, 2, 3]

print("Combinations:")
for combination in combinations(array, 2):
    print(combination)

def permutations(array: list[int], ties=1):
    if ties < 1:
        return [[]]

    merged = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], ties - 1):
            merged.append((value, *edges))

    return merged

array = [1, 2, 3]

print("Permutations:")
for permutation in permutations(array, 2):
    print(permutation)
