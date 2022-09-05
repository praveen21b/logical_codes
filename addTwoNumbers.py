def solution(l1,l2):
    
    n1 = int(''.join(''.join(str(ele) for ele in l1)))
    n2 = int(''.join(''.join(str(ele) for ele in l2)))
    
    res = str(n1+n2)[::-1]
    return [int(ele) for ele in res]


print(solution([0],[0])) #[0]
print(solution([9,9,9,9,9,9,9],[9,9,9,9])) #[8,9,9,9,0,0,0,1]
print(solution([2,4,3],[5,6,4])) # [7,0,8]