def combinations(array, tie):
    if tie == 0:
        return [[]]

    answer = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], tie - 1):
            answer.append((value, *edges))

    return answer


array = [1, 2, 3, 4, 5]
tie = 3

print(combinations(array, tie))
