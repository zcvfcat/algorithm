def fib_fast_doubling(n):
    """빠른 두배법으로 n번째 피보나치 수 (0-index) 반환"""
    if n < 0:
        raise ValueError("n은 음수가 될 수 없습니다.")

    def _fib(k):
        if k == 0:
            return (0, 1)
        a, b = _fib(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k & 1:
            return (d, c + d)
        else:
            return (c, d)

    return _fib(n)[0]


