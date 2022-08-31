# Maximize the number N by inserting '5' at any position


def solution(N):
    if N >= 0:
        new = []
        digit_checked = str(N)
        mode = 1
    else:
        mode = -1
        new = ['-']
        digit_checked = str(N)[1:]

    for i, ele in enumerate(digit_checked):
        if (5*mode) < (int(ele)*mode):
            new.append(ele)
        else:
            new.append(str(5))
            new.append(digit_checked[i:])
            break
    else:
        new.append(str(5))
    
    
    
    return (new, digit_checked)
 
print(solution(0))
