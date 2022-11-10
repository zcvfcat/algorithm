# 시간제한...
n = int(input())
lst = list(map(int, input().split(' ')))
ans = [0] * n
stack = []

for i in range(n):
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

print(''.join(map(lambda x: str(x)+' ', ans)))
