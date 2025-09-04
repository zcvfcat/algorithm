def mod_pow(base, exponent, mod):
    """거듭제곱의 모듈러 값 (빠른 제곱)"""
    if mod <= 0:
        raise ValueError("mod는 양수여야 합니다.")
    base %= mod
    result = 1 % mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return result


def extended_gcd(a, b):
    """확장 유클리드: (g, x, y) 반환. g=gcd(a,b), ax+by=g"""
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    x = old_s if a >= 0 else -old_s
    y = old_t if b >= 0 else -old_t
    return old_r, x, y


def mod_inverse(a, mod):
    """모듈러 역원: a*x ≡ 1 (mod) 해 x 반환. 존재하지 않으면 예외."""
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError("역원이 존재하지 않습니다.")
    return x % mod


