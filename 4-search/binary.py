def binary_search(arr, target):
    """
    이진 탐색: 정렬된 배열에서 target의 인덱스를 찾습니다.

    - arr는 오름차순 정렬이어야 합니다.
    - 반환: target의 인덱스(없으면 -1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(arr, target):
    """
    lower_bound: 정렬된 arr에서 target 이상(>=)이 처음 나오는 인덱스.
    - 반환 값은 [0..len(arr)] 범위에 있음 (없으면 len(arr))
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    """
    upper_bound: 정렬된 arr에서 target 초과(>)가 처음 나오는 인덱스.
    - 반환 값은 [0..len(arr)] 범위에 있음 (없으면 len(arr))
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


