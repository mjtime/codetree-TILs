def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())
hap = 0
for j in range(a, b+1):
    if is_prime(j):
        hap += j
print(hap)