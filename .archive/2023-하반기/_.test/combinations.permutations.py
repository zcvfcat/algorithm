def combinations(array, ties):
    if ties < 1:
        return [[]]
    
    tied = []

    for node, value in enumerate(array):
        for edges in combinations(array[node+ 1:], ties - 1):
            tied.append([value, *edges])
    
    return tied

def permutations(array, ties):
    if ties < 1:
        return [[]]
    
    tied = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], ties - 1):
            tied.append([value, *edges])
    
    return tied

array = [1, 2, 3, 4, 5]
tie = 2

print('순서 없는 조합 nCr')
print(combinations(array, tie))

print('순서 있는 조합 nPr')
print(permutations(array, tie))

