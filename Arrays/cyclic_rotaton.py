# def cyclic_rotation(lst,num):
#     for i in range(0,num):
#         a = lst[0]
#         lst.remove(a)
#         lst.append(a)
#     return lst

# print(cyclic_rotation([7,2,8,3,5],1))
# print(cyclic_rotation([1, 2, 3, 4], 4))

def solution(lst,target):
    new = [0]*len(lst)
    for i in range(0,len(lst)):
        new[(i+target)%len(lst)] = lst[i]
    return new

print(solution([3, 8, 9, 7, 6],3))
print(solution([1, 2, 3, 4], 4))