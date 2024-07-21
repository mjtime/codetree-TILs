def cal_hap(n):
    hap = 0
    for i in range(1, n+1):
        hap += i
    return hap//10

n = int(input())
print(cal_hap(n))