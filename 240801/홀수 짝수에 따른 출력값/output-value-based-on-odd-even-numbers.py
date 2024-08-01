def hap(n):
    if n < 1:
        return 0
    return hap(n-2) + n

n = int(input())
print(hap(n))