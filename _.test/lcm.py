# greatest common divisor 
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

# lowest common multiple
def lcm(a, b):
    return (a * b) // gcd(a, b) # 정수여야함
