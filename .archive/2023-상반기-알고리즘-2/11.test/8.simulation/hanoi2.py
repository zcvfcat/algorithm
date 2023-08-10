# O(2^n)
def hanoi(n, start, end, via):
    if n == 1:
        return 1

    count = 0

    count += hanoi(n - 1, start, via, end)
    count += hanoi(n - 1, via, end, start)

    return count
