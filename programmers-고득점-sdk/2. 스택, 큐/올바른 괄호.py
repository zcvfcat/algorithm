def solution(string):
    open_count = 0

    for char in string:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1

            if open_count < 0:
                return False

    is_close = open_count == 0

    return is_close


print(solution("()()") == True)
print(solution("(())()") == True)
print(solution(")()(") == False)
print(solution("(()(") == False)
