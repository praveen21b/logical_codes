def sum_of_natural_numbars(target):
    total = 0
    for num in range(1,target+1):
        total += num
    return total

print(sum_of_natural_numbars(6))