def solution(n, times):
    ans = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            ans = mid
            right = mid - 1
        elif people < n:
            left = mid + 1

    return ans


print(solution(6, [7, 10]) == 28)
