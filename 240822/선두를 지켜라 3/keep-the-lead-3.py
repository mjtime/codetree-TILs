# 동일시점, 같은 방향
# N, M번 걸쳐 특정 속도, 시간만큼 이동
# 매 시간 현재 선두인 사람 카운트
# 총 카운트 출력
MAX_LEN = 1000001
n, m = map(int, input().split())
arr_a = [0 for _ in range(MAX_LEN)]
arr_b = [0 for _ in range(MAX_LEN)]

idx_a = 1
idx_b = 1
def move(arr, num, idx):
    for _ in range(num):
        v, t = map(int, input().split())
        for j in range(t):
            arr[idx] = arr[idx-1]+v
            idx += 1
    return idx

idx_a = move(arr_a, n, idx_a)
idx_b = move(arr_b, m, idx_b)

cnt = 1
race = [0 for _ in range(idx_a-1)]
for i in range(1, idx_a):
    if arr_a[i] == arr_b[i]:
        race[i-1] = 3
    elif arr_a[i] > arr_b[i]:
        race[i-1] = 1
    else:
        race[i-1] = 2

for i in range(1, len(race)):
    if race[i] != race[i-1]:
        cnt += 1
print(cnt)