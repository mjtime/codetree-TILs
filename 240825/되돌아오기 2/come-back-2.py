# 0,0 N 방향
# (입력)L왼쪽 90도 변경, R 오른쪽 90도 변경, F 전진
# 1칸/s, 회전/s
# (출력)처음 위치로 돌아오는데 소요되는 시간, 아니면 -1

dxs, dys =[0, 1, 0, -1],[1, 0, -1, 0]
x, y = 0, 0
num_dic = 3

dics = list(input())

cnt = 0
check = False
for d in dics:
    cnt += 1
    if d == 'F':
        x = x+dxs[num_dic]
        y = y+dys[num_dic]

        if x == 0 and y == 0:
            check = True
            break

    elif d == 'L':
        num_dic = (num_dic+3)%4
    else:
        num_dic = (num_dic+1)%4

if check:
    print(cnt)
else:
    print(-1)