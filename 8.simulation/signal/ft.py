import math


def fourier_transform(x):
    N = len(x)
    X = []
    for k in range(N):
        # X(k)를 계산합니다.
        Xk = 0
        for n in range(N):
            Xk += x[n] * math.e**(-1j * 2 * math.pi * k * n / N)
        X.append(Xk)
    return X


# 사용 예시
if __name__ == "__main__":
    x = [1, 2, 3, 4]
    result = fourier_transform(x)
    print(result)
