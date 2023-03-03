def window_slice(arr, k):
    """
    리스트 arr에서 길이가 k인 윈도우를 이동하면서 해당 윈도우 내 요소들의 최댓값을 리스트로 반환하는 함수.
    """
    max_values = []
    n = len(arr)
    if k <= 0 or k > n:
        # k가 유효하지 않은 경우 예외 처리
        return max_values
    for i in range(n - k + 1):
        # 윈도우의 시작 인덱스 i를 이동하면서 모든 윈도우에 대해 최댓값 찾기
        window_values = arr[i:i+k]
        max_values.append(max(window_values))
    
    return max_values

# 테스트 코드
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(window_slice(arr, k))  # [3, 3, 5, 5, 6, 7]
