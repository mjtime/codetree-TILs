n, m = map(int, input().split())
list_a = list(map(int, input().split()))

def cal(m):
    hap = 0
    while m>0:
        hap += list_a[m-1]
        
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return hap

    
print(cal(m))