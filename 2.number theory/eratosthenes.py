def eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False

    result = []
    for i in range(2, n + 1):
        if prime[i]:
            result.append(i)
    
    return result
