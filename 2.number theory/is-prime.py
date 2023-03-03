def is_prime(number):
    if number < 2:
        return False

    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


print(1, is_prime(1))
print(2, is_prime(2))
print(3, is_prime(3))
print(4, is_prime(4))
print(5, is_prime(5))
print(6, is_prime(6))
print(7, is_prime(7))
