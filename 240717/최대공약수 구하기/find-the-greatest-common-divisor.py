def cal_gcd(n, m):
    for i in range(min(n,m),1,-1):
        if n % i == 0 and  m % i == 0:
            return i


n, m = map(int, input().split())
print(cal_gcd(n,m))