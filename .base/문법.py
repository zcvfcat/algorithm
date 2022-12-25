import sys
from collections import Counter, defaultdict
print(list(map(lambda x: x + 10, [1, 2, 3])))

print({key: value for key, value in {'a': 2, 'b': 3}.items()})


# def get_natural_number():
#     n = 0
#     while True:
#         n += 1
#         yield n


# g = get_natural_number()

# for _ in range(0, 100):
#     print(next(g), end=' ')

# a = [n for n in range(1000000)]
# b = range(1000000)

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# k = [1, 2, 3, 4, 5, 6, 1, 2, 3]

# i = 0
# for v in k:
#     print(i, v)
#     i += 1

# for i, v in enumerate(k):
#     print(i, v)

# print(5/3)
# print(5//3)
# print(5 % 3)
# print(divmod(5, 3))

# print('1', '2', '3', sep=',')

# a = ['A', 'B']
# print(' '.join(a))
# print('{0}: {1}'.format(10, 20))

a = [1, 2, 3, 4, 5, 6, 7, 7, 7, 6, 4]

b = Counter(a)
print(b.most_common(2))  # 빈도가 높은 것 두 개
