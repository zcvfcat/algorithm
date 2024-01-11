def combinations(arr, tie):
    if tie < 1:
        return [[]]
    
    tied = []

    for node, value in enumerate(arr):
        for edges in combinations(arr[node + 1:], tie - 1):
            tied.append((value, *edges))
    
    return tied

array = [1, 2, 3, 4, 5]
tie = 3

print(combinations(array, tie))
