# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, 
# publication or disclosure prohibited.

def solution(A):
    n = len(A)
    counter = [0] * n
    for i in range(0, n):
        #print(i)
        if (A[i] > 0) and (A[i] <= n):
            counter[A[i] - 1] += 1
    print(counter)

    for i in range(0, len(counter)):
        if (counter[i] == 0):
            return i + 1
    return n + 1

print(solution([1,3,1]))