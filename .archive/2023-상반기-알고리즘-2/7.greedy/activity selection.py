def activity_selection(activities):
    # 종료 시간이 빠른 순서대로 정렬한다.
    sorted_activities = sorted(activities, key=lambda x: x[1])
    result = [sorted_activities[0]]

    for activity in sorted_activities:
        # 마지막으로 선택한 활동과 겹치지 않으면 추가
        if activity[0] >= result[-1][1]:
            result.append(activity)

    return result

activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
print(activity_selection(activities))
