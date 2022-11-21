def eratosthenes(length=100):
    primes = [number for number in range(1, length)]

    for step in range(2, length + 1):
        if step == 0:
            continue

        for number in range(step, length, step):
            if number == step:
                continue

            primes[number - 1] = 0

    return [*map(lambda x: True if x != 0 else False, primes)]
    # return [*filter(lambda x: x != 0, primes)]


print(eratosthenes(100))
