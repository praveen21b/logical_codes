def solution(S):
    valid = True
    stack = []

    for i in S:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()

        else: 
            valid = False

    return 1 if valid and not stack else 0

print(solution(')()'))
print(solution(''))