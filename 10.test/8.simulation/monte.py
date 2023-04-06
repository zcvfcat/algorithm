import random

n = 10000000
count = 0

for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y <= x ** 2:
        count += 1

result = count / n * 4

print(result)

# 먼저, 몬테 카를로 알고리즘은 확률을 이용하여 함수를 근사하는 방법 중 하나입니다.

# 해당 알고리즘은 다음과 같은 과정을 거칩니다.

# 적분하려는 함수를 정의합니다.
# 적분 범위에 해당하는 사각형을 그립니다.
# 사각형 내부에 무작위 점들을 생성합니다. 이 때, 생성된 점들은 균등한 분포를 가져야 합니다.
# 생성된 점들 중 함수 내부에 위치한 점들의 비율을 계산합니다.
# 계산된 비율과 사각형 넓이를 곱하여 적분 값을 추정합니다.
# 이렇게 추정된 값은 실제 적분값과 차이가 있을 수 있지만, 생성된 점들의 개수가 충분히 많다면 추정값은 실제 값에 근접할 가능성이 높아집니다.

# 위와 같은 방식으로 몬테 카를로 알고리즘은 다양한 문제에 적용될 수 있으며, 특히 면적, 부피, 적분 등에서 사용됩니다.