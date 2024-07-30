def cal(n):
    if n < 10:
        return n ** 2
    
    return cal(n//10)+(n%10)**2

n = int(input())
print(cal(n))