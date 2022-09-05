# def highestPowerOf2(n):
 
#     return (n & (~(n - 1)))
 
 
# #Driver code
# if __name__=='__main__':
#     n = 48
#     print(highestPowerOf2(n))

# A positive integer N is given. The goal is to find the highest power of 2 that divides N. In other words, we have to find the maximum K for which N modulo 2^K is 0.

# For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the highest power of 2 that divides N.

# For example, given integer N = 24, the function should return 3, as explained above.

# Assume that:

# N is an integer within the range [1..1,000,000,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(N:int)->int:
    # odd or even check
    if N % 2 != 0:
        return 0 # 2**0=1
    counter = 0
    while (N % (2**counter)) == 0:
        counter += 1

    return counter-1

print(solution(24))
print(solution(48))