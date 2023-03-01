def permutations(array, tie):
    if tie == 0:
        return [[]]

    answer = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], tie - 1):
            answer.append((value, *edges))

    return answer


array = [1, 2, 3, 4, 5]
tie = 2

print(permutations(array, tie))
