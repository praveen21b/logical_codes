# 66% Detected time complexity:O(N*M)
# def solution(N,A):
#     counter = [0]*N
#     max_val = 0
#     for i in A:
#         print(i)
#         if i > N:
#             max_val = max(counter)
#             print(max_val)
#             counter = [max_val]*N
#             continue
#         counter[i-1] += 1
#     return counter

def solution(N,A):
    counter = [0]*N
    start = 0
    max_val = 0
    for i in A:
        idx = i-1
        if i > N:
            start = max_val
        elif counter[idx] < start:
            counter[idx] = start + 1

        #increaement
        else:
            counter[idx] += 1

        # updating max_val
        if i <= N and counter[idx] > max_val:
            max_val = counter[idx]

    for i in range(len(counter)):
        if counter[i] < start:
            counter[i] = start

    return (counter)

print(solution(5, [3,4,4,6,1,4,4])) # [3, 2, 2, 4, 2]