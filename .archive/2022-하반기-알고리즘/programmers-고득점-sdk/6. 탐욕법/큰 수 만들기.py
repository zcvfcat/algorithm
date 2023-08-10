def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            print(stack)
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack[:len(stack) - k])


# print(solution("1924", 2) == "94")
print(solution("1231234", 3) == "3234")
# print(solution("4177252841", 4) == "775841")
