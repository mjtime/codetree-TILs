ARR_LEN = 200000
arr_num = [[0,0] for _ in range(ARR_LEN)] #[white, black]
arr_color = ['N' for _ in range(ARR_LEN)]
now = ARR_LEN // 2
n = int(input())
for i in range(n):
    color = 'N'
    color_num = -1
    go, dic = input().split()
    go = int(go)
    if dic == 'R':
        go = now + go
        color = 'B'
        color_num = 1
    else:
        go = now - go
        color = 'W'
        color_num = 0
    
    start = min(go, now)
    end = max(go, now)

    for i in range(start, end):
        if arr_color[i] == 'G':
            break
        arr_num[i][color_num] += 1
        arr_color[i] = color
        if arr_num[i][0] >= 2 and arr_num[i][1] >=2:
            arr_color[i] = 'G'
    if dic == 'R':
        now = end
    else:
        now = start
    # print(arr_num[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
    # print()

# print(arr_num[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
# print(arr_color[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
print(arr_color.count('W'), arr_color.count('B'), arr_color.count('G'))