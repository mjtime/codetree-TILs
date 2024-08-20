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
check = False
for i in range(1, min(len(arr_a), len(arr_b))):
    if arr_a[i] == arr_b[i] and check==False:
        cnt += 1
        check = True
    else:
        check=False

print(cnt)