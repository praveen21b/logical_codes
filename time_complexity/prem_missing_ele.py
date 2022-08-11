def solution(A):
    n = len(A) + 1
    if n == 1:
        return 1
    
    return (n * (n+1)) // 2 - sum(A)


print(solution([2, 3, 1, 5]))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(solution([]))
print(solution([5]))