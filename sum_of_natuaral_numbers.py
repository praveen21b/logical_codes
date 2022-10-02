# def sum_of_natural_numbars(target):
#     total = 0
#     for num in range(1,target+1):
#         total += num
#     return total

def sum_of_natural_numbars(target):
    return (target/2)*(1+target)

print(sum_of_natural_numbars(6))