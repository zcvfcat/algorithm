def counting_sort(arr, max_value=None):
    if not arr:
        return arr

    if min(arr) < 0:
        raise ValueError("counting_sort는 음이 아닌 정수 배열에만 사용할 수 있습니다.")

    if max_value is None:
        max_value = max(arr)

    count = [0] * (max_value + 1)
    for value in arr:
        if value < 0:
            raise ValueError("counting_sort는 음이 아닌 정수 배열에만 사용할 수 있습니다.")
        if value > max_value:
            # max_value가 명시된 경우 대비
            count.extend([0] * (value - max_value))
            max_value = value
        count[value] += 1

    # 누적합으로 변환 (안정 정렬)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for value in reversed(arr):
        count[value] -= 1
        output[count[value]] = value

    for i in range(len(arr)):
        arr[i] = output[i]
    return arr


