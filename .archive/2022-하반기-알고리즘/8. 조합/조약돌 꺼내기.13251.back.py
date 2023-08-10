d = [0] * 51
probability = [0] * 51

m = int(input())
d = [*map(int, input().split())]
t = 0

for i in range(0, m):
    t += d[i]

k = int(input())
ans = 0

for i in range(0, m):
    if d[i] >= k:
        probability[i] = 1
        for j in range(0, k):
            probability[i] = probability[i] * (d[i] - j)/(t - j)

        ans += probability[i]

print(ans)
