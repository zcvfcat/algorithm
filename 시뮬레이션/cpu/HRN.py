class Job:
    def __init__(self, time, priority):
        self.time = time
        self.priority = priority


jobs = [Job(1, 5), Job(2, 3), Job(3, 2), Job(4, 4), Job(5, 7), Job(6, 5), Job(7, 6), Job(8, 9), Job(9, 8)]
n = 9


def HRN_Algorithm(jobs, n):
    # jobs는 job의 번호들을 담고 있는 배열, n은 배열의 크기
    # 이 함수는 다음과 같이 작업을 수행하는 것을 목표로 합니다.
    # 1. 모든 job들을 먼저 우선순위를 매긴 뒤 정렬합니다.
    # 2. 각 job들을 독립적으로 수행합니다.
    # 3. 모든 job이 완료될 때까지 계속합니다.

    # 우선순위를 정하기 위해 각 job의 작업 시간과 우선순위를 계산합니다.
    time = [0] * n
    priority = [0] * n
    for i in range(n):
        time[i] = jobs[i].time
        priority[i] = 1.0 + float(time[i]) / jobs[i].priority

    # 각 job을 우선순위에 따라 정렬합니다.
    for i in range(n):
        for j in range(n - 1 - i):
            if priority[j] < priority[j + 1]:
                priority[j], priority[j + 1] = priority[j + 1], priority[j]
                jobs[j], jobs[j + 1] = jobs[j + 1], jobs[j]

    # 모든 job을 독립적으로 수행합니다.
    result = 0
    for i in range(n):
        result += time[i] * (n - i)

    # 결과를 반환합니다.
    return result


print(HRN_Algorithm(jobs, n))
