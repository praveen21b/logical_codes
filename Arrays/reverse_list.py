def revere_list(A:list)->list:
    n = len(A)
    for i in range(n//2):
        k = n - i - 1
        A[i], A[k] = A[k],A[i]
    return A

print(revere_list([1,2,3,4,5]))
 
"""or Use A.reverse() or list(reversed(A))"""