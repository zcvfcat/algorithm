from collections import deque


def radix_sort(unsorted):
    buckets = [deque() for _ in range(10)]
    max_num = max(unsorted)
    digit = 1
    q = deque(unsorted)

    while max_num >= digit:
        while q:
            num = q.popleft()
            buckets[(num // digit) % 10].append(num)

        for bucket in buckets:
            while bucket:
                q.append(bucket.popleft())

        digit *= 10

    return list(q)


array = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sortedArray = radix_sort(array)

print(sortedArray)
