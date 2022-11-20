from collections import Counter


def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return [*diff.keys()][0]


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]) == "leo")
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"]) == "vinko")
print(solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]) == "mislav")
