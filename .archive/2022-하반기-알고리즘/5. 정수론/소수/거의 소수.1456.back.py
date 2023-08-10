n, m = map(int, input().split(' '))
a = [0] * 10000001  # root(10^14) = 10^7

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i] == 0:
        continue

    for j in range(i + i, len(a), i):
        a[j] = 0

count = 0

for i in range(2, 10000001):
    if a[i] != 0:
        target = a[i]
        while a[i] <= m / target:
            if a[i] >= n / target:
                count += 1
            target = target * a[i]

print(count)
