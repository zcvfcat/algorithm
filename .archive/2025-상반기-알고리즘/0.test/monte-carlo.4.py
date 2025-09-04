import random
import math

# 몬테 카를로 시뮬레이션 함수
def monte_carlo_pi(num_samples):
    inside_circle = 0
    
    # num_samples만큼 점을 찍습니다
    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        # 점이 원 안에 있는지 확인합니다
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # 사분원에 있는 점들의 비율을 통해 π를 추정합니다
    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# 예시: 1,000,000개의 점을 사용하여 π 추정
num_samples = 1000000
pi_estimate = monte_carlo_pi(num_samples)
print(f"Estimated Pi value: {pi_estimate}")

# 실 측정할때 혹은 구현시 사용