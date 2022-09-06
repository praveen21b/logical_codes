# Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

# Examples:

# 1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer. Your function may return any correct answer.

# 2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

# 3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

# Assume that:

# A and B are integers within the range [0..100];
# at least one solution exists for the given A and B.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(A,B):

    # check for which letter need to occur more
    string = ''
    i = 1
    counter = A+B
    while i <= counter:
        print(i)
        if string[-2:] == 'aa':
            # add 'b'
            B -= 1
            string += 'b'
        elif string[-2:] == 'bb':
            # add 'a'
            A -= 1
            string += 'a'
        
        elif A>=B:
            A -= 1
            string += 'a'
        
        else: # start with 'a'
            B -= 1
            string += 'b' # added string
        i+=1
        #print(i)
    return string

print(solution(A=3,B=2))