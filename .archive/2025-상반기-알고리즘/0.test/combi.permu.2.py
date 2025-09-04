def combinations(arr,ties):
    if ties < 1:
        return arr
    
    tied = []

    for node, value in enumerate(arr):
        for edges in combinations(arr[node + 1:],ties - 1):
            tied.append((value, *edges))
    
    return tied

def permutations(arr,ties):
    if ties < 1:
        return arr
    
    tied = []

    for node, value in enumerate(arr):
        for edges in permutations(arr[:node] + arr[node + 1:],ties - 1):
            tied.append((value, *edges))
    
    return tied