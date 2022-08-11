# 66% correct
# from collections import Counter

# def solution(A):
#     counts = Counter(A)
#     values = list(counts.values())
#     return list(counts.keys())[values.index(min(values))]

# 66% score found time complexity O(n2)
# def solution(A):
#     new = []
#     for i in A:
#         if i not in new:
#             new.append(i)
#         else:
#             new.remove(i)
#     return new[0]

def solution(A):
    numbers = set()
    for n in A:
        if n in numbers:
            numbers.discard(n)
        else:
            numbers.add(n)
    return numbers.pop()
print(solution([9,3,9,3,9,7,9]))
