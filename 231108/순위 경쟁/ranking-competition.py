n = int(input())
users = {'A':0, 'B':1, 'C':2}
record = [0, 0, 0]
max_score = 0
cnt = -1
answer=0
record_num = 1
user_check=0
def check_score(cnt):
    if cnt == 3:
        return 1
    elif cnt == 2:
        if record[0] == record[1]:
            return 2
        elif record[0] == record[2]:
            return 3
        elif record[1] == record[2]:
            return 4
    elif cnt == 1:
        return 5

for _ in range(n):
    c, s =input().split()
    record[users[c]] += int(s)
    max_score = max(record)
    cnt = record.count(max_score)

    user_check = check_score(cnt)

    if user_check == 5:
        idx = record.index(max_score)
        if idx == 0:
            user_check = 5
        elif idx == 1:
            user_check = 6
        elif idx == 2:
            user_check = 7
    
    if record_num != user_check:
        answer += 1
        record_num = user_check
print(answer)