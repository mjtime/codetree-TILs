ARR_LEN = 200000
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
        arr_color[i] = color

print(arr_color.count('W'), arr_color.count('B'))