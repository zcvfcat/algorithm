def binary(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

def binary_recursive(array, target, low, high):
    if low > high:
        return None

    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_recursive(array, target, mid + 1, high)
    else:
        return binary_recursive(array, target, low, mid - 1)

def test_binary_search():
    # 테스트 케이스 1: 타겟이 배열에 존재하는 경우
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary(array, target)
    assert result == 4, f"Expected 4, but got {result}"

    # 테스트 케이스 2: 타겟이 배열의 처음에 존재하는 경우
    target = 1
    result = binary(array, target)
    assert result == 0, f"Expected 0, but got {result}"

    # 테스트 케이스 3: 타겟이 배열의 끝에 존재하는 경우
    target = 9
    result = binary(array, target)
    assert result == 8, f"Expected 8, but got {result}"

    # 테스트 케이스 4: 타겟이 배열에 존재하지 않는 경우
    target = 10
    result = binary(array, target)
    assert result is None, f"Expected None, but got {result}"

    # 테스트 케이스 5: 빈 배열
    array = []
    target = 1
    result = binary(array, target)
    assert result is None, f"Expected None, but got {result}"

    # 테스트 케이스 6: 중복된 값이 있는 배열에서 첫 번째로 발견된 인덱스를 반환하는지 확인
    array = [1, 2, 4, 4, 4, 5, 6]
    target = 4
    result = binary(array, target)
    assert result in [2, 3, 4], f"Expected one of [2, 3, 4], but got {result}"

    print("All test cases passed!")

# 테스트 함수 실행
test_binary_search()