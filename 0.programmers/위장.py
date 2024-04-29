from collections import Counter
from functools import reduce


def solution(clothes):
    count = Counter([kind for _, kind in clothes])
    ans = reduce(lambda acc, curr: acc + curr + acc * curr, count.values())
    return ans
