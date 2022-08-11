def equilibrium(A):
    sum_left = A[0]
    sum_right = sum(A[1:])
    diff = abs(sum_right - sum_left)
    for i in range(1, len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]
        new_diff = abs(sum_right - sum_left)
        # if diff > new_diff:
        #     diff = new_diff
        diff = min(diff,new_diff)
    return diff

print(equilibrium([3,1,2,4,3]))