n = int(input())
max_cnt = -1
cnt = 1
before = -1
for _ in range(n):
    num = int(input())
    if num == before:
        cnt += 1
    else:
        before = num
        max_cnt = max(max_cnt, cnt)
        cnt = 1
print(max_cnt)