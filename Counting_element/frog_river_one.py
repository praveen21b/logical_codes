def solution(X, A):
    steps = set(range(1,X+1))

    for idx, val in enumerate(A):
        if val in steps:
            steps.discard(val)
            if not steps:
                return idx
    return -1