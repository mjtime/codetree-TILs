def divide(n):
    if n == 1:
        return 0
    
    if n % 2== 0:
        return divide(n//2) + 1
    else:
        return divide(n//3) + 1

n = int(input())
print(divide(n))