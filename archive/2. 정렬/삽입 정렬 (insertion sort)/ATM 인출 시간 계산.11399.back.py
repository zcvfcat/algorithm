# from functools import reduce

# n = int(input())
# array = list(map(int, input().split()))

# sorted_array = sorted(array)

# r = reduce(lambda acc, curr: [*acc, acc[-1] + curr], sorted_array, [0])
# print(sum(r))

from functools import reduce

n = int(input())
array = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]

r = reduce(lambda acc, curr: [*acc, acc[-1] + curr], array, [0])

print(sum(r))
