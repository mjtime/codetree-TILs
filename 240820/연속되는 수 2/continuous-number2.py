n = int(input())
max_cnt = 1
cnt = 1
before = -1
for i in range(n):
    num = int(input())
    if i == 0:
        before = num
        continue
    if num == before:
        cnt += 1
    else:
        before = num
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)