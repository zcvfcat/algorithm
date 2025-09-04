from collections import Counter

def solution(participant,completion):
    diff = Counter(participant) - Counter(completion)

    return [*diff.keys()][0]