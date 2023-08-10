import cmath


def fft(x):
    # 입력 신호의 길이가 1 이하일 경우, 입력 신호를 반환합니다.
    if len(x) <= 1:
        return x

    # 입력 신호의 길이를 반으로 나눕니다.
    half_n = len(x) // 2
    # 반으로 나눈 입력 신호를 이용하여 재귀 호출합니다.
    even = fft(x[0:half_n])
    odd = fft(x[half_n:])

    # 재귀 호출 결과를 이용하여 FFT 알고리즘을 적용합니다.
    # w_n^k를 미리 계산합니다.
    w = [cmath.exp(-2j * cmath.pi * k / len(x)) for k in range(half_n)]
    for k in range(half_n):
        t = even[k]
        x[k] = t + w[k] * odd[k]
        x[k + half_n] = t - w[k] * odd[k]

    # FFT 결과를 반환합니다.
    return x


# 사용 예시
if __name__ == "__main__":
    x = [1, 2, 3, 4]
    result = fft(x)
    print(result)
