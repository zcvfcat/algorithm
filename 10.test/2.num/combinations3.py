def combinations3(array, time):
    if time < 1:
        return [[]]

    ties = []

    for node, value in enumerate(array):
        for edges in combinations3(array[node + 1:], time - 1):
            ties += [(value, *edges)]

    return ties


array = [1, 2, 3, 4, 5]
tie = 3

print(combinations3(array, tie))
