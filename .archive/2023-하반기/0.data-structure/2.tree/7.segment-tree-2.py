from math import ceil, log


def init(tree, N):
    for i in range(N - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


def query(tree, N, left, right):
    result = 0
    left += N
    right += N

    while left < right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 1:
            result += tree[right - 1]
            right -= 1
        left //= 2
        right //= 2
    return result


def update(tree, N, i, val):
    tree[N + i] = val
    i += N
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


nums = [1, 3, 5, 2, 6, 4]
segment_tree = [0] * (2 * len(nums))
N = len(nums)

for i in range(len(nums)):
    segment_tree[N + i] = nums[i]
init(segment_tree, N)

update(segment_tree, N, 1, 4)
nums[1] = 4
