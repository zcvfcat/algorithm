def solution(numbers: list):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    return str(int(''.join(map(lambda x: str(x), numbers))))


print(solution([6, 10, 2]) == "6210")
print(solution([3, 30, 34, 5, 9]) == "9534330")
