ARR_LEN = 200000
arr_num = [[0,0] for _ in range(ARR_LEN)] #[white, black]
arr_color = ['N' for _ in range(ARR_LEN)]
before_dic = 'N'
now = ARR_LEN // 2
n = int(input())
for i in range(n):
    color = 'N'
    color_num = -1
    go, dic = input().split()
    go = int(go)
    if i == 0:
        before_dic = dic
    if dic == 'R':
        if dic != before_dic:
            now -= 0
        else:
            now -= 1
        go = now + go
        color = 'B'
        color_num = 1
    else:
        if dic != before_dic:
            now -= 0
        else:
            now += 1
        go = now - go
        color = 'W'
        color_num = 0
    
    start = min(go, now)
    end = max(go, now)
    # print(start, end)
    for i in range(start, end):
        # if i == end - 1:
        #     if dic == 'R':
        #         now = end
        #     else:
        #         now = end - i
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
    before_dic = dic
    # print('now>',now)
    # print(arr_num[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
    # print()

# print(arr_num[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
# print(arr_color[ARR_LEN//2 - 5: ARR_LEN//2 + 6])
print(arr_color.count('W'), arr_color.count('B'), arr_color.count('G'))