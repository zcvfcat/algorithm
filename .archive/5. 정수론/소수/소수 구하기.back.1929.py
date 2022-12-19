M, N = map(int, input().split())
a = [0] * (N + 1)


for i in range(2, N + 1):
    a[i] = i

for i in range(2, int(N ** 0.5) + 1):
    if a[i] == 0:
        continue

    for j in range(i + i, N + 1, i):
        a[j] = 0

for i in range(M, N + 1):
    if a[i] != 0:
        print(a[i])
