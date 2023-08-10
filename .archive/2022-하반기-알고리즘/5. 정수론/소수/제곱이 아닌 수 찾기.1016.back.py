n, m = map(int, input().split())
a = [False] * (m - n + 1)

for i in range(2, int(m ** 0.5) + 1):
    pow = i * i
    start_index = int(n / pow)
    if n % pow != 0:
        start_index += 1

    for j in range(start_index, int(m / pow) + 1):
        a[int(j * pow) - n] = True

count = 0

for i in range(0, m - n + 1):
    if not a[i]:
        count += 1

print(count)
