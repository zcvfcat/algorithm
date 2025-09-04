def linear_search(arr, target):
    """
    선형 탐색: 배열을 처음부터 끝까지 보며 target을 찾습니다.

    - 반환: target의 첫 인덱스(없으면 -1)
    - 정렬 여부와 상관없이 동작합니다.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_all(arr, target):
    """target이 등장하는 모든 인덱스를 리스트로 반환합니다."""
    return [i for i, v in enumerate(arr) if v == target]


