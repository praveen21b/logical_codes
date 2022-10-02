def fib(n): # nth fibonacci number
    if n == 1:
        return 0
    if n <= 3:
        return 1
    return fib(n-1)+fib(n-2)
    
        
print(fib(5))
