def combinations(array, tie):
    ans =[]

    if tie ==0 :
        return [ans]
    
    for i in range(len(array)):
        node = array[i]

        for edges in combinations(array[i + i:], tie - 1):
            ans.append((node, *edges))
    
    return ans


print(combinations([0,1,2,3,4],2))