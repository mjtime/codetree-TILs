user={'A':0, 'B':1}
record = [1, 1]
state = 1
cnt = 0
n = int(input())
for _ in range(n):
    c, s = input().split()
    record[user[c]] += int(s)
    if record[0] == record[1]:
        check = 1
    elif record[0]<record[1]:
        check = 2
    else:
        check = 3
    if check != state:
        cnt += 1
        state = check
print(cnt)