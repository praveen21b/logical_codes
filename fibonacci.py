# def fib(n): # nth fibonacci number
#     if n == 1:
#         return 0
#     if n <= 3:
#         return 1
#     return fib(n-1)+fib(n-2)

def fib(n):
    fib_ser = [0,1]
    for i in range(n-2):
        if i < len(fib_ser):
            fib_ser.append(fib_ser[-1]+fib_ser[-2])
    return fib_ser

print(fib(5))
