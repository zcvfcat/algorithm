def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    
def memo_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a