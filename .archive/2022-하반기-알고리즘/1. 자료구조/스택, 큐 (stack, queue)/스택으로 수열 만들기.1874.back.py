n = int(input())

stack = []
ans = ''
curr = 1

for i in range(n):
    now = int(input())
    while now >= curr:
        stack.append(curr)
        ans += '+\n'
        curr += 1

    n = stack.pop()
    if n >= now:
        ans += '-\n'
    else:
        ans = 'NO'
        break

print(ans)
