# pro1
def solution(A):
    return list(dict.fromkeys(A))  

print(solution([1, 2, 0, 1, 3, 2]))

# prob2
def solution1(S):
    S = S.split(',')
    total = []
    for i in S:
        if i.isdigit():
            total.append(float(i))
        elif i.startswith('-'):
            total.append(-float(i[1:]))
    #print(total)
    return int(sum(total)/len(total)) if len(total) else 0

print(solution1('1,2.5,e,3'))
print(solution1('1,-2.5,e,30'))



