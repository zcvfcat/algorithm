def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def memorized_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    
    return a
