def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return False

    return True
