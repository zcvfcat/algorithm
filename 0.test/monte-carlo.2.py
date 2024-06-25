import random

# 총 점의 수
n = 10 ** 6
count = 0

# n개의 무작위 점을 생성하고 원 내부에 있는 점의 수를 센다
for _ in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1:
        count += 1

# 원 내부에 있는 점의 비율을 계산
ratio = count / n

# 비율에 4를 곱하여 원의 넓이를 근사
area_of_circle = ratio * 4

print(area_of_circle)