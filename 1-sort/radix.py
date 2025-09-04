def radix_sort(arr):
    # 빈 배열이면 바로 반환
    if not arr:
        return arr

    # 음수 있으면 에러
    if min(arr) < 0:
        raise ValueError("radix_sort는 음이 아닌 정수 배열에만 사용할 수 있습니다.")

    # 가장 큰 수 찾기
    max_num = max(arr)
    exp = 1  # 1의 자리부터 시작

    # 자리수별로 반복
    while max_num // exp > 0:
        # 0~9까지 숫자별로 버킷 만들기
        buckets = [[] for _ in range(10)]

        # 각 숫자를 해당 자리수 기준으로 버킷에 넣기
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # 버킷을 차례대로 합쳐서 arr에 다시 저장
        idx = 0
        for bucket in buckets:
            for num in bucket:
                arr[idx] = num
                idx += 1

        # 다음 자리수로 이동
        exp *= 10

    return arr
