import random

n = 1000000
count = 0

for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y <= x ** 2:
        count += 1

result = count / (n * 4)
