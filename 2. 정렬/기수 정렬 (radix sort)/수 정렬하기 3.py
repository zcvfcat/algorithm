# 오 이렇게 생각할 수도 있네;;
import sys
input = sys.stdin.readline

n = int(input())
max_width = 10001

count = [0] * max_width

for i in range(n):
    count[int(input())] += 1

for i in range(max_width):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
