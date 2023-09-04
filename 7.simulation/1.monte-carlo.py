"""
    몬테 카를로 시뮬레이션
        확률적 시뮬레이션을 사용하여 미지의 결과를 추정
    
    시간 복잡도
        샘플 수에 따라 다름
    
    사용 이유
        복잡한 문제 해결
            몬테 카를로 시뮬레이션은 수학적으로 해결하기 어려운 또는 해석하기 어려운 복잡한 문제를 다룰 때 유용
            확률적 시뮬레이션을 통해 실제 현상을 모방하고 그 결과를 추정함으로써 문제를 다룸

        결과 예측
            미지의 결과를 예측하기 위해 사용
            금융 분야에서는 옵션 가격, 주가 움직임 등을 예측하고 물리학에서는 입자 동력학, 양자 현상 등을 모델링하고 예측하는 데 사용

        실험적인 접근
            실험적 데이터를 생성하거나 가설을 검증

        확률적 분석
            확률 분포를 시뮬레이션하여 이론적 분석과 비교

        대규모 데이터 생성
            대량의 데이터를 생성하고 분석하는 데 사용
            기계 학습 모델을 훈련하거나 복잡한 통계 분석을 수행하는 데 필요한 데이터를 얻을 수 있음

        최적화
            몬테 카를로 기법은 최적화 문제를 다룰 때 사용
            가능한 해의 공간을 무작위로 탐색하고 최적의 해를 찾는 데 활용

        환경 모델링
            환경 모델링 및 시뮬레이션에서는 몬테 카를로 기법을 사용하여 자연 현상을 모방하고 예측하여 환경 변화 및 자원 관리에 대한 결정을 지원

"""
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
