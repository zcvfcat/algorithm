def ternary_search_real(f, left, right, iterations=100):
    """
    삼분 탐색(연속 구간): f가 [left, right] 구간에서 단봉(한 번만 최대/최소)일 때 최대값 위치를 찾습니다.

    - 반환: (best_x, f(best_x)) 근사값
    - iterations 횟수만큼 구간을 줄입니다.
    - 기본은 최대값을 찾도록 구현되어 있습니다.
      (최소값을 찾으려면 f 대신 -f를 넣거나 비교 방향을 바꾸세요.)
    """
    for _ in range(iterations):
        m1 = (2 * left + right) / 3
        m2 = (left + 2 * right) / 3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    best_x = (left + right) / 2
    return best_x, f(best_x)


def ternary_search_int(f, left, right):
    """
    삼분 탐색(정수 구간): f가 [left, right]에서 단봉일 때 최대값의 정수 위치를 찾습니다.

    - 반환: (best_x, f(best_x)) 정확한 정수 위치 탐색(잔여 2~3개 구간 완전탐색)
    """
    while right - left >= 3:
        m1 = (2 * left + right) // 3
        m2 = (left + 2 * right) // 3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    best_x = left
    best_val = f(best_x)
    for x in range(left + 1, right + 1):
        val = f(x)
        if val > best_val:
            best_x, best_val = x, val
    return best_x, best_val


