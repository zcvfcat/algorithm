def prime_number(n):
    # 0, 1 은 소수 아님
    if n < 2:
        return False
    
    # 계산상 root(n) + 1 중 나누어 떨어질시 소수 아님
    for i in range(2, int(n**0.5) + 1, 1):
        if n % i == 0:
            return False
    
    return True