def equilibrium(A:list):
    idx = {}
    diff = 0
    for i in range(1,len(A)):
        sum_left = sum(A[:i])
        sum_right = sum(A[i:])
        piv_diff = abs(sum_right-sum_left)
        if diff == 0:
            diff+=piv_diff
            idx[i] = diff
        elif diff > piv_diff:
            diff = piv_diff
            idx[i] = diff
    min_diff = min(idx.values())
    return list(idx.keys())[list(idx.values()).index(min_diff)]

print(equilibrium([3,1,2,4,3]))