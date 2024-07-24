a, b = map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def hap_is_even(n):
    hap = (n//10)+(n%10)
    if hap % 2 == 0:
        return True
    else:
        return False

cnt = 0

for i in range(a, b+1):
    if hap_is_even(i) and is_prime(i):
        cnt += 1

print(cnt)