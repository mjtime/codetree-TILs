def cal(n):
    if n == 1:
        return 1
    return cal(n-1) + n

n = int(input())
print(cal(n))