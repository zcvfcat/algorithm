import bisect


def lis_length(nums):
    """
    가장 긴 증가 부분 수열 길이 (O(n log n), Patience sorting)
    - 입력: 정수 리스트
    - 반환: LIS 길이
    """
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


