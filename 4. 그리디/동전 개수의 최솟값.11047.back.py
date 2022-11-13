N, K = map(int, input().split(' '))
coins = [0] * N

for i in range(N):
    coins[i] = int(input())

count = 0

for i in range(N - 1, -1, -1):
    if coins[i] <= K:
        count += K//coins[i]
        K = K % coins[i]

print(count)
