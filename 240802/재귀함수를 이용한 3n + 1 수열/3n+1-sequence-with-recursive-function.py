def counter(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return counter(n//2) + 1
    else:
        return counter(n * 3 + 1) + 1

n = int(input())
print(counter(n))