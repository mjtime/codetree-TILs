n, b = map(int, input().split())
arr = []

while True:
    if n < 1:
        break
    
    arr.append(n % b)
    n //= b

for bit in arr[::-1]:
    print(bit, end='')