# 모르겠네;;

def solution(numbers):
    min_max = [0, 0]
    sum_value = 0
    for idx in range(len(numbers)-1, -1, -1):
        if numbers[idx] == '+':
            continue

        elif numbers[idx] == '-':
            temp_min, temp_max = min_max
            min_max[0] = min(-(sum_value + temp_max), -sum_value+temp_min)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(numbers[idx+1])

            min_max[1] = max(-(sum_value + temp_min), -minus_v + (sum_value-minus_v) + temp_max)
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(numbers[idx]) >= 0:
            sum_value += int(numbers[idx])
    min_max[1] += sum_value
    return min_max[1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]) == 1)
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]) == 3)
