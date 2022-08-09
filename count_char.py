from collections import Counter

input_str = 'aaaabbbcccz'
# Output = '4a3b3c1z'

op_str = ''
for keys, values in (Counter(input_str)).items():
    op_str+=(str(values)+keys)
print(op_str)
