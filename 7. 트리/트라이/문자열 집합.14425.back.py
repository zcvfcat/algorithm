import sys

input = sys.stdin.readline

n, m = map(int, input().split())
texts = set([input() for _ in range(n)])

count = 0

for _ in range(m):
    text = input()

    if text in texts:
        count += 1

print(count)
