def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a % b)

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    