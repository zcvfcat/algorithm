def max_subarray_sum(nums):
    """
    카데인 알고리즘: 연속 부분배열 최대 합
    - 시간: O(n), 공간: O(1)
    """
    best = float('-inf')
    cur = 0
    for x in nums:
        cur = max(x, cur + x)
        if cur > best:
            best = cur
    return best


