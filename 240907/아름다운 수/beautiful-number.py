# 1~4로 이루어진 수
# 아름다운 수? 해당 숫자만큼 해당 수가 연속으로 나오는 경우

n = int(input())
arr = []
ans = 0

def check_beauty():
    global ans
    check_num = -1 # 확인 기준이 되는 수
    cnt = 0 # 확인 기준이 되는 수가 총 몇개 있는가
    beauty = False
    for i in range(n):
        if i == 0:
            check_num = arr[i]
            cnt = check_num -1
        else:
            # 해당 숫자가 연속으로 나오지 않은 경우
            if arr[i] != check_num and cnt != 0:
                break
            # 해당 숫자가 연속으로 나오는 경우 -1
            elif arr[i] == check_num and cnt != 0:
                cnt -= 1
            # cnt가 0인데 새로운 수를 만나면(배열이 안 끝났으면),
            # 기준이 되는 수와 cnt 업데이트
            elif cnt == 0:
                check_num = arr[i]
                cnt = check_num -1
        # cnt가 0인 상태로 배열이 끝났으면 아름다운 수
        if i == n-1 and cnt == 0:
            beauty = True
    if beauty:
        ans += 1
            
def choose(curr_num):
    if curr_num == n+1:
        check_beauty()
        return
    # 1 ~ 4의 숫자로 이루어진 수
    for i in range(1, 5):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()
    return

choose(1)
print(ans)