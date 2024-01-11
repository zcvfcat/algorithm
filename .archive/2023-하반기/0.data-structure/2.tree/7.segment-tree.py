"""
    세그먼트 트리
"""

from math import ceil, log


def init(arr, tree, i, left, right):
    if left == right:
        tree[i] = arr[left]
        return tree[i]

    mid = (left + right) // 2
    tree[i] = init(arr, tree, i * 2, left, mid) + init(arr, tree, i * 2 + 1, mid + 1, right)

    return tree[i]


def search(tree, i, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[i]
    mid = start + (end - start) // 2

    return search(tree, i * 2, start, mid, left, right) + search(tree, i * 2 + 1, mid + 1, end, left, right)


def update(tree, i, start, end, idx, diff):
    if start > idx or idx > end:
        return
    tree[i] += diff
    if start != end:
        mid = start + (end - start) // 2
        update(tree, i * 2, start, mid, idx, diff)
        update(tree, i * 2 + 1, mid + 1, end, idx, diff)


nums = [1, 3, 5, 2, 6, 4]
segment_tree = [0] * pow(2, ceil(log(len(nums), 2) + 1))

init(nums, segment_tree, 1, 0, len(nums) - 1)
