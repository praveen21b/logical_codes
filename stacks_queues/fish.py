def solution(A, B):

    # list to store upstream fishes
    stack = []
    # downstream fishes survival count
    survived = 0

    for i in range(0,len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            if stack:
                while stack and stack[-1] < A[i]:
                    stack.pop()
                if not stack:
                    survived += 1
            else: 
                survived += 1
    return len(stack) + survived

print(solution([4,3,2,1,5],[0,1,1,0,1]))