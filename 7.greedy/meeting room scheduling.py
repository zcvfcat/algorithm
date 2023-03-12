def schedule(meetings):
    # 시작 시간을 기준으로 정렬
    sorted_meetings = sorted(meetings, key=lambda x: x[0])

    # 첫 번째 회의 배치
    result = [sorted_meetings[0]]
    end_time = sorted_meetings[0][1]

    # 다음 회의 배치
    for i in range(1, len(sorted_meetings)):
        if sorted_meetings[i][0] >= end_time:
            result.append(sorted_meetings[i])
            end_time = sorted_meetings[i][1]

    return result
