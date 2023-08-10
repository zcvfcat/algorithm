import random

n = 100000  # 시행 횟수 설정
count = 0  # (0,0)~(1,1) 범위 내에 랜덤하게 생성된 점의 개수

for i in range(n):
    x = random.uniform(0, 1)  # 0~1 범위의 랜덤값 생성
    y = random.uniform(0, 1)
    if y <= x**2:  # y값이 x^2 값보다 작으면 (x,y)는 함수 상 위에 위치함
        count += 1

result = count/n * 4  # 4로 곱해줌으로써 사각형의 넓이인 1을 대략적으로 나타낼 수 있음
print(result)
