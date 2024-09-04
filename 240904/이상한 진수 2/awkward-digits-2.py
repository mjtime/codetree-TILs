# 0을 만나면 1로 변경
# 0이 없는 경우 가장 왼쪽 1을 0으로 변경
# 이후 2진법 -> 10진법 변경

n = list(map(int, input()))

zero_check = False
for i in range(1, len(n)):
    if n[i] == 0:
        n[i] = 1
        zero_check = True
        break

if not zero_check:
    n[len(n)-1] = 0

ten = 0
for bit in n:
    ten = ten*2 + bit

print(ten)