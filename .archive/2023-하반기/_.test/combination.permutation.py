def combinations(arr, tie):
    if tie < 1:
        return [[]]

    tied = []

    for idx, node in enumerate(arr):
        for edges in combinations(arr[idx + 1:], tie - 1):
            tied.append((node, *edges))

    return tied

def permutations(arr, tie):
    if tie < 1:
        return [[]]
    
    tied = []

    for idx, node in enumerate(arr):
        for edges in permutations(arr[:idx] + arr[idx + 1:], tie - 1):
            tied.append((node, *edges))
    
    return tied

array = [1, 2, 3, 4, 5]
tie = 2

print(combinations(array, tie))
