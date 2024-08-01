def f(n):
    if n < 3:
        return 1
    
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))