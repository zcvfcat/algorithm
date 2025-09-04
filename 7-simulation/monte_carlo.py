import random


def estimate_pi(num_samples=100000):
    """
    몬테카를로로 원주율 PI 추정.
    - [0,1]x[0,1] 정사각형에서 임의의 점을 찍어, 1/4 원 내부 비율을 측정
    - 내부 점 비율 * 4 ≈ PI
    """
    inside = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / num_samples


