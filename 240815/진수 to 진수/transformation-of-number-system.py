a, b = map(int, input().split())
n = list(map(int, input()))

ten = 0
for bit in n:
    ten = ten * a + bit

base_b = []
while True:
    if ten < 1:
        break
    base_b.append(ten % b)
    ten //= b

for bit in base_b[::-1]:
    print(bit, end='')