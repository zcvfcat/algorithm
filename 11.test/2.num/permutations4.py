def permutations(array, tie):
    if tie < 1:
        return [[]]

    tied = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], tie - 1):
            tied += [(value, *edges)]

    return tied


array = [1, 2, 3, 4, 5]
tie = 3

print(permutations(array, tie))
