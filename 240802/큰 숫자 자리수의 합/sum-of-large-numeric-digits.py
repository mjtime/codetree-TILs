def hap(n):
    if n <10:
        return n
        
    return hap(n//10)+n%10

a, b, c = map(int, input().split())
print(hap(a*b*c))