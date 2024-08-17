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
        start = now
        end = now + go
        color, color_num = 'B', 1
        now = end - 1
    else:
        start = now - go + 1
        end = now + 1
        color, color_num = 'W', 0
        now = start
    
    for i in range(start, end):
        if arr_color[i] == 'G':
            continue
        arr_num[i][color_num] += 1
        arr_color[i] = color
        if arr_num[i][0] >= 2 and arr_num[i][1] >=2:
            arr_color[i] = 'G'

print(arr_color.count('W'), arr_color.count('B'), arr_color.count('G'))