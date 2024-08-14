binary = list(map(int, input()))
ten = 0

for bit in binary:
    ten = ten * 2 + bit

ten *= 17
new_binary = []

while True:
    if ten < 1:
        break
    new_binary.append(ten % 2)
    ten //= 2

for bit in new_binary[::-1]:
    print(bit, end='')