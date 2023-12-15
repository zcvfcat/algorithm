def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd2(a,b):
    while b !=0:
        a, b = b, a % b
    
    return a
    