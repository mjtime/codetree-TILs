n, m = map(int, input().split())
arr_a = [0]
arr_b = [0]

def move(arr, num):
    for _ in range(num):
        t, d = input().split()
        t = int(t)
        go = 0
        if d == 'L':
            go = -1
        else:
            go = 1
        for _ in range(t):
            arr.append(arr[len(arr)-1] + go)

move(arr_a, n)
move(arr_b, m)

cnt = 0
check = True
max_arr = 0
idx_a = 0
idx_b = 0
for i in range(1, max(len(arr_a), len(arr_b))):

    if arr_a[idx_a] == arr_b[idx_b] and check==False:
        cnt += 1
        check = True
    elif arr_a[idx_a] == arr_b[idx_b] and check==True:
        check = True
    else:
        check=False
    if idx_a < len(arr_a) - 1:
        idx_a += 1
    if idx_b < len(arr_b) - 1:
        idx_b += 1

print(cnt)