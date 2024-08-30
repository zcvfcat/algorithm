from collections import deque

def merge(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = deque(merge(array[:mid])), deque(merge(array[mid:]))

    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())

    return [*merged, *left, *right]

def test_merge():
    # 테스트 케이스 1: 일반적인 정렬된 배열
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(array)
    result = merge(array)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    
    # 테스트 케이스 2: 이미 정렬된 배열
    array = [1, 2, 3, 4, 5]
    expected = array
    result = merge(array)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"

    # 테스트 케이스 3: 역순으로 정렬된 배열
    array = [5, 4, 3, 2, 1]
    expected = sorted(array)
    result = merge(array)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"

    # 테스트 케이스 4: 모든 요소가 같은 배열
    array = [2, 2, 2, 2, 2]
    expected = array
    result = merge(array)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"

    # 테스트 케이스 5: 빈 배열
    array = []
    expected = array
    result = merge(array)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"

    # 테스트 케이스 6: 하나의 요소만 있는 배열
    array = [42]
    expected = array
    result = merge(array)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"

    print("All tests passed!")

# 테스트 실행
test_merge()