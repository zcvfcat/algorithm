def fib_memo(n, _cache=None):
    """
    피보나치 수열 (메모이제이션)
    - 입력: n >= 0
    - 반환: F(n)
    - 시간/공간: O(n)
    """
    if n < 0:
        raise ValueError("n은 음수가 될 수 없습니다.")
    if _cache is None:
        _cache = {0: 0, 1: 1}
    if n in _cache:
        return _cache[n]
    _cache[n] = fib_memo(n - 1, _cache) + fib_memo(n - 2, _cache)
    return _cache[n]


def fib_bottom_up(n):
    """
    피보나치 수열 (보텀업 DP)
    - 입력: n >= 0
    - 반환: F(n)
    - 시간: O(n), 공간: O(1)
    """
    if n < 0:
        raise ValueError("n은 음수가 될 수 없습니다.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


