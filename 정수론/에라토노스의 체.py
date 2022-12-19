
def eratos(length):
    if length < 1:
        return []

    prime_array = [True] * (length + 1)
    prime_array[0] = False
    prime_array[1] = False

    for number in range(2, length):
        if prime_array[number] is False:
            continue

        for i in range(number * number, length, number):
            prime_array[i] = False

    return prime_array


print(eratos(100))
