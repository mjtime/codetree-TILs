# 'carry' is when add num and num, turn over the 10's digit
# ex) 3+6=9(no carry), 11+12=23(no carry), 5+7=12(carry), 81+72=153(carry)
# /print/ maximum value of the sum that can come out without nay carry
#         when 3 different number are chosen.

n = int(input())
arr = [int(input()) for _ in range(n)]
max_num = -1

def cal_digit(num):
    if num > 0:
        return num // 10, num % 10
    else:
        return 0, 0

def check_carry(a, b, c):
    while True:
        if a == 0 and b == 0 and c == 0:
            return True
        a, remain_a = cal_digit(a)
        b, remain_b = cal_digit(b)
        c, remain_c = cal_digit(c)

        if remain_a + remain_b + remain_c > 9:
            return False

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if check_carry(arr[i], arr[j], arr[k]):
                max_num = max(max_num, arr[i]+arr[j]+arr[k])

print(max_num)