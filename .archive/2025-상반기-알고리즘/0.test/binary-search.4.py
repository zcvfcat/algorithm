import bisect

array = sorted([1, 5, 1, 4, 2, 3, 4, 5, 1, 23, 35, 41, 24, 43, 23, 5, 23])

print(bisect.bisect_left(array, 4))
print(bisect.bisect_right(array, 4))