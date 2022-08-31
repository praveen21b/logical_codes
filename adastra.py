# Maximize the number N by inserting '5' at any position


import math

def solution(N):
    # if N >= 0:
    #     new = []
    #     digit_checked = str(N)
    #     mode = 1
    # else:
    #     mode = -1
    #     new = ['-']
    #     digit_checked = str(N)[1:]

    # for i, ele in enumerate(digit_checked):
    #     if (5*mode) < (int(ele)*mode):
    #         new.append(ele)
    #     else:
    #         new.append(str(5))
    #         new.append(digit_checked[i:])
    #         break
    # else:
    #     new.append(str(5))
    # return int(''.join(new))
    

# second solution
    n = len(str(N))
    target = 5
    val = str(N)
    max_val = -math.inf # or 8000
    mode,tar_str = (1,val) if N >= 0 else (-1,val[1:])
    #print(n)
    for i in range(0,n+1):
        value = tar_str[i:] + str(target) + tar_str[:i]
        max_val = max((max_val), (int(value) * mode))
    return max_val
 
print(solution(-999))
print(solution(-128))
print(solution(128))
