n, m = map(int, input().split())
arr_a = [0]
arr_b = [0]

def go_left(arr, num):
    for i in range(num):
        arr.append(arr[len(arr)-1] - 1)

def go_right(arr, num):
    for i in range(num):
        arr.append(arr[len(arr)-1] + 1)

def input_move(arr, n):
    for i in range(n):
        dire, go = input().split()
        go = int(go)
        if dire == 'L':
            go_left(arr, go)
        else:
            go_right(arr, go)

input_move(arr_a, n)
input_move(arr_b, m)

ans = -1
for i in range(1, min(len(arr_a), len(arr_b))):
    if arr_a[i] == arr_b[i]:
        ans = i
        break

print(ans)