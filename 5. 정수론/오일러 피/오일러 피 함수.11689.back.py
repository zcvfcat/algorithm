n = int(input())

target = n

for p in range(2, int(n ** 0.5) + 1):
    if n % p == 0:
        target = target - target / p
        while n % p == 0:
            n /= p

if n > 1:
    target = target - target / n

print(int(target))
