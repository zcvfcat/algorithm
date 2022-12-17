coins = [50, 10, 500, 100, 1000]

target = 52030

coins.sort(reverse=True)

count = 0
for coin in coins:
    count += target // coin
    target = target % coin

print(count)
