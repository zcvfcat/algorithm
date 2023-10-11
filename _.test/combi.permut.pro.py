from itertools import permutations, combinations, product

k = ['2', '0', '0', "0", '1']
l = len(k)

print('nPr 순서가 필요한 경우')
print([*permutations(k, l)])


print('nCr 순서가 필요없는 경우')
print([*combinations(k, l)])

print('product')
print([*product(k, ['2','3'])])
