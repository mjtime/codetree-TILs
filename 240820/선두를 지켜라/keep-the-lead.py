# 특정 속도 특정 시간 a, b가 각각 이동
# 선두가 몇 번 바뀜? ( 어는 한 쪽이 앞서는 경우)

n, m = map(int, input().split())
arr_a = [0]
arr_b = [0]
arr_diff = []
def move(arr, num):
    for _ in range(num):
        v, t = map(int, input().split())
        for _ in range(t):
            arr.append(arr[len(arr)-1]+v)

move(arr_a, n)
move(arr_b, m)

for i in range(1, len(arr_a)):
    if arr_a[i] - arr_b[i] > 0:
        arr_diff.append(1)
    elif arr_a[i] - arr_b[i] < 0:
        arr_diff.append(-1)



cnt = 0
for i in range(1, len(arr_diff)):
    if arr_diff[i] != arr_diff[i-1]:
        cnt += 1

print(cnt)