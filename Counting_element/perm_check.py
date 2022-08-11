def solution(A):
    # """Check if given nums are permutation 1..N."""
    # if not nums:
    #     return 0
    # seen = set()
    # for num in nums:
    #     print(num)
    #     if num < 1 or num > len(nums) or num in seen:
    #         return 0
    #     seen.add(num)
    # return 1

    if len(A) == 0:
        return 0
    new = set()
    for val in A:
        if val > len(A) or (val in new):
            return 0
        new.add(val)
    return 1

print(solution([2,4,3]))