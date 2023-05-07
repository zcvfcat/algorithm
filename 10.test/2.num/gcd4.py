def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def permutations(array, tie):
    if tie == 0:
        return [[]]
    
    ans = []

    for node, value in enumerate(array):
        for edges in permutations(array[:node] + array[node + 1:], tie - 1):
            ans.append((value, *edges))
    
    return ans

def combinations(array, tie):
    if tie == 0:
        return [[]]
    
    ans = []

    for node, value in enumerate(array):
        for edges in combinations(array[node + 1:], tie - 1):
            ans.append((value, *edges))
    
    return ans
