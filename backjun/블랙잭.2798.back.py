import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = [*map(int, input().split())]

select = 0

for three_cards in combinations(cards, 3):
    total = sum(three_cards)

    if total <= m and total > select:
        select = total

print(select)
