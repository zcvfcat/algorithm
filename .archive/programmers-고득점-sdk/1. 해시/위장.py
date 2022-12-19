from collections import Counter
from functools import reduce


def solution(clothes):
    count = Counter([kind for _, kind in clothes])
    ans = reduce(lambda acc, curr: acc + curr + acc * curr, count.values())
    return ans


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5)
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3)
