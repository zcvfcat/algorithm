def is_prime(k):
    if k < 2:
        return False
    
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False

    return True

